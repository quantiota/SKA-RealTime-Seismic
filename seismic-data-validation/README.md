# Seismic Data Stream Validation

Real-time seismic data collection and QuestDB ingestion validation.

## Purpose
- Validate live seismic data streaming from IRIS SeedLink
- Test QuestDB table creation and data ingestion
- Collect clean raw seismic parameters for future SKA analysis

## Usage

```bash
# Test QuestDB connection
python test_connection.py

# Start live data collection
python seismic_stream_validator.py

# Validate collected data
python validate_data.py
```

## Output

- `/logs/seismic_validation.log`
- `questdb-query-1752183200659.csv`


📊 Total samples collected: 104762

📍 Samples per station:
   IU.INCN.10.BHZ: 12993 samples
   II.PFO.10.BHZ: 12242 samples
   IU.HRV.60.BHZ: 12051 samples
   IU.HRV.00.BHZ: 12035 samples
   IU.ANMO.10.BHZ: 11911 samples
   IU.HRV.10.BHZ: 11193 samples
   II.PFO.00.BHZ: 10617 samples
   IU.ANMO.00.BHZ: 10547 samples
   IU.INCN.00.BHZ: 5916 samples
   IU.HRV.70.BHZ: 5257 samples

📈 Amplitude statistics:
   IU.INCN.00.BHZ: -4537.0 to 8058.0 (avg: 1686.0)
   II.PFO.00.BHZ: -119.0 to 944.0 (avg: 437.6)
   IU.ANMO.10.BHZ: 7340.0 to 8097.0 (avg: 7664.8)
   IU.HRV.60.BHZ: 227.0 to 819.0 (avg: 525.1)
   IU.HRV.00.BHZ: -693.0 to 1156.0 (avg: 242.6)
   IU.ANMO.00.BHZ: 1341.0 to 1945.0 (avg: 1592.1)
   IU.HRV.10.BHZ: -886.0 to 1464.0 (avg: 323.7)
   II.PFO.10.BHZ: 2844.0 to 3927.0 (avg: 3413.7)
   IU.HRV.70.BHZ: -4789.0 to -820.0 (avg: -2790.5)
   IU.INCN.10.BHZ: -16811.0 to 79939.0 (avg: 29627.2)

🕐 Recent samples:
   IU.INCN.10.BHZ: 24741.0 at 2025-07-10 21:31:07.869538
   IU.INCN.10.BHZ: 24274.0 at 2025-07-10 21:31:07.844538
   IU.INCN.10.BHZ: 22375.0 at 2025-07-10 21:31:07.819538
   IU.INCN.10.BHZ: 38785.0 at 2025-07-10 21:31:07.794538
   IU.INCN.10.BHZ: 46086.0 at 2025-07-10 21:31:07.769538
   IU.INCN.10.BHZ: 25000.0 at 2025-07-10 21:31:07.744538
   IU.INCN.10.BHZ: 22643.0 at 2025-07-10 21:31:07.719538
   IU.INCN.10.BHZ: 31879.0 at 2025-07-10 21:31:07.694538
   IU.INCN.10.BHZ: 33696.0 at 2025-07-10 21:31:07.669538
   IU.INCN.10.BHZ: 43011.0 at 2025-07-10 21:31:07.644538

🔍 Data quality:
   NULL amplitudes: 0
   NULL station_ids: 0
✅ Data quality PASSED