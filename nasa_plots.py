import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

try:
    conn = psycopg2.connect(
        dbname="newstar_planet1_2",      
        user="postgres",       
        password="152911",
        host="localhost",
        port="5432"
    )
    print("Database connection successful! Fetching data...")
    query = "SELECT planet_name, planet_size_earths, planet_temperature_k_elvin FROM star_planet1;"
    df = pd.read_sql_query(query, conn)
    conn.close()
    print("Data loaded into Python successfully!")
    df['planet_size_earths'] = pd.to_numeric(df['planet_size_earths'], errors='coerce')
    df['planet_temperature_k_elvin'] = pd.to_numeric(df['planet_temperature_k_elvin'], errors='coerce')
    df = df.dropna() 
    sns.set_theme(style="darkgrid")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['planet_size_earths'], kde=True, color='purple', bins=10)
    plt.title('Distribution of Habitable Planet Sizes', fontsize=14, fontweight='bold')
    plt.xlabel('Planet Size (Relative to Earth/Jupiter)', fontsize=12)
    plt.ylabel('Count of Planets', fontsize=12)
    plt.savefig('planet_size_distribution.png')
    plt.show()
    print("Graph 1 saved as 'planet_size_distribution.png'")
    plt.figure(figsize=(10, 6))
    sns.regplot(data=df, x='planet_size_x', y='planet_temperature_k_elvin', color='teal', 
                marker='o', scatter_kws={'s':50}, line_kws={'color':'red'})
    plt.title('Planet Temperature vs Planet Size', fontsize=14, fontweight='bold')
    plt.xlabel('Planet Size', fontsize=12)
    plt.ylabel('Planet Temperature (Kelvin)', fontsize=12)
    plt.savefig('size_vs_temperature.png')
    plt.show()
    print("Graph 2 saved as 'size_vs_temperature.png'")
    top_5_hot = df.nlargest(5, 'planet_temperature_k_elvin')
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top_5_hot, x='planet_temperature_x', y='planet_name', palette='flare')
    plt.title('Top 5 Hottest Habitable Planets', fontsize=14, fontweight='bold')
    plt.xlabel('Temperature (Kelvin)', fontsize=12)
    plt.ylabel('Planet Name', fontsize=12)
    plt.savefig('top_5_hottest_planets.png')
    plt.show()
    print("Graph 3 saved as 'top_5_hottest_planets.png'")
except Exception as e:
    print(f"Oops! Small error occurred: {e}")



