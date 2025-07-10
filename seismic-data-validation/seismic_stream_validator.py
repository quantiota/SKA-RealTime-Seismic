import datetime
import time
import json
import logging
import os
import psycopg2
import psycopg2.pool
import threading
import signal
from concurrent.futures import ThreadPoolExecutor
import traceback
from obspy.clients.seedlink import EasySeedLinkClient
from config import QDB_CONFIG, SEISMIC_CONFIG, LOG_CONFIG  # ✅ Use config

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)


# Configure logging to write to file
logging.basicConfig(
    level=getattr(logging, LOG_CONFIG['level']),
    format=LOG_CONFIG['format'],
    filename=LOG_CONFIG['file'],  # ← This writes to file!
    filemode='a'  # Append to log file
)

# Also log to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter(LOG_CONFIG['format'])
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

# Initialize connection pool using config
connection_pool = psycopg2.pool.SimpleConnectionPool(1, 10, **QDB_CONFIG)




def create_questdb_table():
    """Create seismic_events table in QuestDB."""
    conn = connection_pool.getconn()
    try:
        with conn.cursor() as cur:
            # Drop existing table to ensure correct schema
            cur.execute("DROP TABLE IF EXISTS seismic_events;")
            
            create_table_sql = """
            CREATE TABLE seismic_events (
                network SYMBOL,
                station SYMBOL,
                location SYMBOL,
                channel SYMBOL,
                station_id SYMBOL,
                sample_index LONG,
                amplitude DOUBLE,
                sampling_rate DOUBLE,
                trace_start_time TIMESTAMP,
                trace_end_time TIMESTAMP,
                packet_samples LONG,
                delta DOUBLE,
                timestamp TIMESTAMP
            ) TIMESTAMP(timestamp) PARTITION BY DAY;
            """
            cur.execute(create_table_sql)
            conn.commit()
            logging.info("Clean seismic events table created")
    except Exception as e:
        logging.error(f"Error creating QuestDB table: {e}")
        logging.error(traceback.format_exc())
    finally:
        connection_pool.putconn(conn)

def insert_seismic_sample(trace, sample_index, amplitude, sample_timestamp):
    """Insert seismic sample with raw parameters only."""
    conn = connection_pool.getconn()
    try:
        with conn.cursor() as cur:
            insert_sql = """
            INSERT INTO seismic_events (network, station, location, channel, station_id, 
                                      sample_index, amplitude, sampling_rate, 
                                      trace_start_time, trace_end_time, packet_samples, delta,
                                      timestamp)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            # Extract raw parameters from live stream (no computations)
            network = str(trace.stats.network)
            station = str(trace.stats.station)
            location = str(trace.stats.location) if trace.stats.location else "00"
            channel = str(trace.stats.channel)
            station_id = trace.id
            sampling_rate = float(trace.stats.sampling_rate)
            trace_start_time = trace.stats.starttime.datetime
            trace_end_time = trace.stats.endtime.datetime
            packet_samples = int(trace.stats.npts)
            delta = float(trace.stats.delta)

            sample_data = (
                network,              # network
                station,              # station
                location,             # location (string)
                channel,              # channel
                station_id,           # station_id
                sample_index,         # sample_index
                float(amplitude),     # amplitude
                sampling_rate,        # sampling_rate
                trace_start_time,     # trace_start_time
                trace_end_time,       # trace_end_time
                packet_samples,       # packet_samples
                delta,                # delta
                sample_timestamp      # timestamp (sample time)
            )
            
            cur.execute(insert_sql, sample_data)
            conn.commit()
            
    except Exception as e:
        logging.error(f"Error inserting seismic sample into QuestDB: {e}")
        logging.error(traceback.format_exc())
    finally:
        connection_pool.putconn(conn)

class QuestDBSeismicClient(EasySeedLinkClient):
    """Clean seismic client - raw data collection only."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sample_count = 0
        
    def on_data(self, trace):
        """Handle incoming seismic data - raw collection only."""
        try:
            # Extract trace metadata
            station_id = trace.id
            sampling_rate = float(trace.stats.sampling_rate)
            
            logging.info(f"Processing {station_id} | {len(trace.data)} samples | "
                        f"Rate: {sampling_rate} Hz")
            
            # Process each sample
            trace_start_time = trace.stats.starttime.datetime
            
            for i, amplitude in enumerate(trace.data):
                # Calculate precise sample timestamp
                sample_time_offset = i / sampling_rate
                sample_timestamp = trace_start_time + datetime.timedelta(seconds=sample_time_offset)
                
                # Insert raw sample data only
                insert_seismic_sample(
                    trace=trace,
                    sample_index=i,
                    amplitude=amplitude,
                    sample_timestamp=sample_timestamp
                )
                
                self.sample_count += 1
                
                # Log progress periodically
                if self.sample_count % 500 == 0:
                    logging.info(f"Collected {self.sample_count} raw seismic samples")
                    
        except Exception as e:
            logging.error(f"Error processing seismic trace: {e}")
            logging.error(traceback.format_exc())

def start_seismic_stream_with_reconnect(server_url, streams):
    """Start seismic stream with auto-reconnect."""
    max_retries = 5
    retry_delay = 5  # seconds
    
    for attempt in range(max_retries):
        try:
            logging.info(f"Connecting to {server_url} (attempt {attempt + 1}/{max_retries})")
            
            client = QuestDBSeismicClient(server_url)
            
            # Add all requested streams
            for stream in streams:
                if len(stream) == 3:
                    network, station, channel = stream
                    client.select_stream(network, station, channel)
                    logging.info(f"Selected stream: {network}.{station}.*.{channel}")
                else:
                    logging.warning(f"Invalid stream configuration: {stream}")
            
            logging.info(f"Starting raw seismic data collection from {server_url}")
            client.run()
            
            # If we reach here, connection was closed normally
            logging.info(f"Seismic stream {server_url} closed normally")
            break
            
        except Exception as e:
            logging.error(f"Seismic stream connection failed for {server_url}: {e}")
            if attempt < max_retries - 1:
                logging.info(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff
            else:
                logging.error(f"Max retries reached for {server_url}")
                break

def shutdown(signum, frame):
    """Handle shutdown signals."""
    logging.info(f"Received shutdown signal: {signum}")
    connection_pool.closeall()
    logging.info("Connection pool closed")
    os._exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    # Create clean QuestDB table
    create_questdb_table()


    logging.info("Starting CLEAN seismic data stream processor...")
    logging.info(f"Target streams: {SEISMIC_CONFIG['streams']}")  # ✅ Use config
    logging.info("✅ Raw data collection only")
    logging.info("✅ No SKA computations")
    logging.info("✅ Fixed location parameter mapping")
    
    # Start clean seismic stream
    with ThreadPoolExecutor(max_workers=1) as executor:
        executor.submit(
            start_seismic_stream_with_reconnect,
            SEISMIC_CONFIG['server'],    # ✅ Use config
            SEISMIC_CONFIG['streams']    # ✅ Use config
        )