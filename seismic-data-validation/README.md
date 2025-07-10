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



## Data Collection Summary

**Total samples collected:** `104,762`



### 📡 Samples per Station

| Station        | Samples |
| -------------- | ------: |
| IU.INCN.10.BHZ |  12,993 |
| II.PFO.10.BHZ  |  12,242 |
| IU.HRV.60.BHZ  |  12,051 |
| IU.HRV.00.BHZ  |  12,035 |
| IU.ANMO.10.BHZ |  11,911 |
| IU.HRV.10.BHZ  |  11,193 |
| II.PFO.00.BHZ  |  10,617 |
| IU.ANMO.00.BHZ |  10,547 |
| IU.INCN.00.BHZ |   5,916 |
| IU.HRV.70.BHZ  |   5,257 |



### 📈 Amplitude Statistics

| Station        | Min     | Max    | Avg      |
| -------------- | ------- | ------ | -------- |
| IU.INCN.00.BHZ | -4,537  | 8,058  | 1,686.0  |
| II.PFO.00.BHZ  | -119    | 944    | 437.6    |
| IU.ANMO.10.BHZ | 7,340   | 8,097  | 7,664.8  |
| IU.HRV.60.BHZ  | 227     | 819    | 525.1    |
| IU.HRV.00.BHZ  | -693    | 1,156  | 242.6    |
| IU.ANMO.00.BHZ | 1,341   | 1,945  | 1,592.1  |
| IU.HRV.10.BHZ  | -886    | 1,464  | 323.7    |
| II.PFO.10.BHZ  | 2,844   | 3,927  | 3,413.7  |
| IU.HRV.70.BHZ  | -4,789  | -820   | -2,790.5 |
| IU.INCN.10.BHZ | -16,811 | 79,939 | 29,627.2 |


### 🕐 Recent Samples

| Station        | Amplitude | Timestamp                  |
| -------------- | --------- | -------------------------- |
| IU.INCN.10.BHZ | 24,741.0  | 2025-07-10 21:31:07.869538 |
| IU.INCN.10.BHZ | 24,274.0  | 2025-07-10 21:31:07.844538 |
| IU.INCN.10.BHZ | 22,375.0  | 2025-07-10 21:31:07.819538 |
| IU.INCN.10.BHZ | 38,785.0  | 2025-07-10 21:31:07.794538 |
| IU.INCN.10.BHZ | 46,086.0  | 2025-07-10 21:31:07.769538 |
| IU.INCN.10.BHZ | 25,000.0  | 2025-07-10 21:31:07.744538 |
| IU.INCN.10.BHZ | 22,643.0  | 2025-07-10 21:31:07.719538 |
| IU.INCN.10.BHZ | 31,879.0  | 2025-07-10 21:31:07.694538 |
| IU.INCN.10.BHZ | 33,696.0  | 2025-07-10 21:31:07.669538 |
| IU.INCN.10.BHZ | 43,011.0  | 2025-07-10 21:31:07.644538 |



### 🔍 Data Quality

* NULL amplitudes: `0`
* NULL station\_ids: `0`
* **✅ Data quality PASSED**

