# src/database_utils.py

import sqlite3
import pandas as pd

def create_earthquake_table(db_path="data/database.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS earthquakes (
        id TEXT PRIMARY KEY,
        time TEXT,
        place TEXT,
        region TEXT,
        mag REAL,
        depth REAL,
        latitude REAL,
        longitude REAL,
        type TEXT,
        url TEXT
    );
    """)
    conn.commit()
    conn.close()

def insert_earthquake_data(df: pd.DataFrame, db_path="data/database.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql("earthquakes", conn, if_exists="replace", index=False)
    conn.commit()
    conn.close()

def query_most_powerful_earthquake(db_path="data/database.db"):
    conn = sqlite3.connect(db_path)
    query = """
    SELECT place, mag, time FROM earthquakes
    ORDER BY mag DESC
    LIMIT 1;
    """
    result = pd.read_sql(query, conn)
    conn.close()
    return result
