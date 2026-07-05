import os
import pandas as pd
import psycopg2
DB_CONFIG = {
    'dbname': 'sharath',
    'user': 'postgres',
    'password': '152911',
    'host': 'localhost',
    'port': '5432'
}
CSV_FILE_PATH = r'C:\Users\shara\pythonstart\freshstart.py\habitable_planets.csv'  
def get_db_connection():
    """Establishes and returns a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except psycopg2.DatabaseError as e:
        print(f"[ERROR] Database connection failed: {e}")
        return None
def load_csv_to_dataframe(file_path):
    """Loads data from a CSV file into a Pandas DataFrame."""
    if not os.path.exists(file_path):
        print(f"[ERROR] Source file not found at: {file_path}")
        return None
    try:
        df = pd.read_csv(file_path)
        print(f"[INFO] Successfully read {len(df)} rows from CSV.")
        return df
    except Exception as e:
        print(f"[ERROR] Failed to read CSV file: {e}")
        return None
def insert_data_to_db(cursor, dataframe):
    """Iterates through the DataFrame and inserts rows into PostgreSQL."""
    insert_query = """
    INSERT INTO habitable_planets (planet_id,planet_name,planet_status,planet_size_earths,planet_temperature_k_elvin,orbital_period_days,orbital_period_upper_err1,orbital_period_lower_err2 )
    VALUES (%s, %s, %s, %s,%s,%s,%s,%s);
    """
    print("[INFO] Ingesting data into PostgreSQL... Please wait...") 
    for _, row in dataframe.iterrows():
        cursor.execute(insert_query, (
            row['planet_id'],
            row['planet_name'], 
            row['planet_status'], 
            row['planet_size_earths'],
            row['planet_temperature_k_elvin'],
            row['orbital_period_days'],
            row['orbital_period_upper_err1'],
            row['orbital_period_lower_err2']
        ))
def main():
    print("=== Starting NASA Data Pipeline ===")
    df = load_csv_to_dataframe(CSV_FILE_PATH)
    if df is None:
        return
    conn = get_db_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()    
        insert_data_to_db(cursor, df)
        conn.commit()
        print("=== 🔥 Pipeline Executed Successfully! Data Loaded to pgAdmin. 🔥 ===")
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