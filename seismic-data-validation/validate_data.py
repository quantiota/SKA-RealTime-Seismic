"""Validate collected seismic data in QuestDB."""
import psycopg2
from config import QDB_CONFIG

def validate_seismic_data():
    """Run validation queries on collected seismic data."""
    try:
        conn = psycopg2.connect(**QDB_CONFIG)
        
        with conn.cursor() as cur:
            # Check if table exists
            cur.execute("SHOW TABLES;")
            tables = [table[0] for table in cur.fetchall()]
            
            if 'seismic_events' not in tables:
                print("❌ seismic_events table not found")
                return
            
            # Total sample count
            cur.execute("SELECT COUNT(*) FROM seismic_events;")
            total_samples = cur.fetchone()[0]
            print(f"📊 Total samples collected: {total_samples}")
            
            # Samples per station
            cur.execute("""
                SELECT station_id, COUNT(*) as sample_count 
                FROM seismic_events 
                GROUP BY station_id 
                ORDER BY sample_count DESC;
            """)
            station_counts = cur.fetchall()
            print("\n📍 Samples per station:")
            for station, count in station_counts:
                print(f"   {station}: {count} samples")
            
            # Amplitude ranges per station
            cur.execute("""
                SELECT station_id, 
                       MIN(amplitude) as min_amp,
                       MAX(amplitude) as max_amp,
                       AVG(amplitude) as avg_amp
                FROM seismic_events 
                GROUP BY station_id;
            """)
            amplitude_stats = cur.fetchall()
            print("\n📈 Amplitude statistics:")
            for station, min_amp, max_amp, avg_amp in amplitude_stats:
                print(f"   {station}: {min_amp:.1f} to {max_amp:.1f} (avg: {avg_amp:.1f})")
            
            # Recent samples
            cur.execute("""
                SELECT station_id, amplitude, timestamp 
                FROM seismic_events 
                ORDER BY timestamp DESC 
                LIMIT 10;
            """)
            recent_samples = cur.fetchall()
            print("\n🕐 Recent samples:")
            for station, amplitude, timestamp in recent_samples:
                print(f"   {station}: {amplitude:.1f} at {timestamp}")
            
            # Data quality checks
            cur.execute("SELECT COUNT(*) FROM seismic_events WHERE amplitude IS NULL;")
            null_amplitudes = cur.fetchone()[0]
            
            cur.execute("SELECT COUNT(*) FROM seismic_events WHERE station_id IS NULL;")
            null_stations = cur.fetchone()[0]
            
            print(f"\n🔍 Data quality:")
            print(f"   NULL amplitudes: {null_amplitudes}")
            print(f"   NULL station_ids: {null_stations}")
            
            if null_amplitudes == 0 and null_stations == 0:
                print("✅ Data quality PASSED")
            else:
                print("⚠️  Data quality issues detected")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Data validation failed: {e}")

if __name__ == "__main__":
    validate_seismic_data()