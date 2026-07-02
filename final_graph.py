import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def generate_database_chart():
    connection = None
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="152911",       
            host="127.0.0.1",
            port="5432",
            database="newstar_planet1_2"   
        )
        query = "SELECT planet_status, planet_size_earths FROM star_planet1;"
        df = pd.read_sql_query(query, connection)
        print("[INFO] Data successfully fetched from PostgreSQL database.")
        df['planet_size_earths'] = pd.to_numeric(df['planet_size_earths'], errors='coerce')
        df = df.dropna(subset=['planet_status', 'planet_size_earths'])
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='planet_status', y='planet_size_earths', data=df, palette='coolwarm')
        plt.title('Planet Size Distribution by Planet Status', fontsize=14, fontweight='bold', pad=15)
        plt.xlabel('Planet Status', fontsize=12, labelpad=10)
        plt.ylabel('Planet Size (Earths)', fontsize=12, labelpad=10)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        output_filename = 'final_database_chart.png'
        plt.savefig(output_filename, dpi=300)
        print(f"[SUCCESS] Chart successfully generated and saved as '{output_filename}'.")
        plt.show()

    except Exception as error:
        print(f"[ERROR] Critical pipeline failure during execution: {error}")

    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL database connection closed safely.")

if __name__ == "__main__":
    generate_database_chart()