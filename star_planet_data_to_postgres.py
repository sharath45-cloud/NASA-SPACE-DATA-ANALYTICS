import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values  

DB_CONFIG = {
    'dbname': 'sharath',
    'user': 'postgres',
    'password': '152911',
    'host': 'localhost',
    'port': '5432'
}

CSV_FILE_PATH = r'C:\Users\shara\OneDrive\Desktop\NASA-SPACE-DATA-ANALYTICS\star_planet1.csv'
def get_db_connection():
    """Establishes and returns a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.DatabaseError as e:
        print(f"[ERROR] Database connection failed: {e}")
        return None

def load_and_clean_dataframe(file_path):
    """Loads CSV and handles dynamic cleaning for all 50 columns without missing any."""
    if not os.path.exists(file_path):
        print(f"[ERROR] Source file not found at: {file_path}")
        return None
    try:
        df = pd.read_csv(file_path)
        print(f"[INFO] Successfully read {len(df)} rows from CSV.")
        df.columns = df.columns.str.replace(' ', '').str.strip()
        
        if 'orbital_period_days' in df.columns:
            df['orbital_period_days'] = 0
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].fillna('Unknown')
            else:
                df[col] = df[col].fillna(0)
                
        return df
    except Exception as e:
        print(f"[ERROR] Failed to read/clean CSV file: {e}")
        return None

def insert_data_dynamic(cursor, dataframe, table_name="star_planet_data"):
    """Dynamically builds query for all 50 columns and inserts using high-speed bulk ingest."""
    columns = ", ".join(dataframe.columns)
    
    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES %s;"
    
    value_tuples = [tuple(x) for x in dataframe.to_numpy()]
    
    print(f"[INFO] Dynamically ingesting all {len(dataframe.columns)} columns into {table_name}... Please wait...") 

    execute_values(cursor, insert_query, value_tuples)

def main():
    print("=== Starting NASA Data Pipeline ===")
    
    df = load_and_clean_dataframe(CSV_FILE_PATH)
    if df is None:
        return
        
    conn = get_db_connection()
    if conn is None:
        return
        
    try:
        cursor = conn.cursor()    
        insert_data_dynamic(cursor, df, table_name="star_planet_data")
        
        conn.commit()
        print("=== Pipeline Executed Successfully! All 50 Columns Loaded to pgAdmin. ===")
    except Exception as e:
        print(f"[CRITICAL] Pipeline failed during execution: {e}")
        if conn:
            conn.rollback()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
        print("[INFO] Database connections closed safely.")

if __name__ == "__main__":
    main()