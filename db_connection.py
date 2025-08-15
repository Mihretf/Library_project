import mysql.connector
from db_config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

if __name__ == "__main__":
    conn = get_connection()
    print("Connected to database:", conn.is_connected())
    conn.close()