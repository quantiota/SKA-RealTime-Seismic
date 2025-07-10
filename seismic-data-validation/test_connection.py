"""Test QuestDB connection and table operations."""
import psycopg2
from config import QDB_CONFIG

def test_questdb_connection():
    """Test basic QuestDB connection and operations."""
    try:
        conn = psycopg2.connect(**QDB_CONFIG)
        
        with conn.cursor() as cur:
            # Test connection
            cur.execute("SELECT 1;")
            result = cur.fetchone()
            print(f"✅ QuestDB connection successful: {result}")
            
            # List tables
            cur.execute("SHOW TABLES;")
            tables = cur.fetchall()
            print(f"📋 Existing tables: {[table[0] for table in tables]}")
            
            # Test table creation
            cur.execute("DROP TABLE IF EXISTS test_seismic;")
            cur.execute("""
                CREATE TABLE test_seismic (
                    station_id SYMBOL,
                    amplitude DOUBLE,
                    timestamp TIMESTAMP
                ) TIMESTAMP(timestamp);
            """)
            print("✅ Test table creation successful")
            
            # Clean up
            cur.execute("DROP TABLE test_seismic;")
            print("✅ Test table cleanup successful")
            
        conn.close()
        print("🎯 QuestDB validation PASSED")
        
    except Exception as e:
        print(f"❌ QuestDB connection failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    test_questdb_connection()