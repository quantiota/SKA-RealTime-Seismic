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

- /logs/seismic_validation.log
- questdb-query-1752183200659.csv