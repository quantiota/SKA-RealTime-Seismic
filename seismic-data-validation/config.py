"""Configuration for seismic data validation."""
import os

# QuestDB Configuration
QDB_CONFIG = {
    'dbname': os.getenv('QDB_PG_NAME', 'qdb'),
    'user': os.getenv('QDB_PG_USER', 'admin'),
    'password': os.getenv('QDB_PG_PASSWORD', 'quest'),
    'host': os.getenv('QDB_PG_HOST', '192.168.1.216'),
    'port': os.getenv('QDB_PG_PORT', '8812')
}

# Seismic Stream Configuration
SEISMIC_CONFIG = {
    'server': 'rtserve.iris.washington.edu',
    'streams': [
        ('IU', 'INCN', 'BHZ'),  # South Korea - High activity
        ('IU', 'ANMO', 'BHZ'),  # New Mexico - Baseline
        ('CI', 'SVD', 'EHZ'),   # California - San Andreas
        ('IU', 'HRV', 'BHZ'),   # Harvard - East Coast
        ('II', 'PFO', 'BHZ'),   # Pinon Flat - California
    ]
}

# Logging Configuration
LOG_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s %(levelname)s %(message)s',
    'file': 'logs/seismic_validation.log'
}