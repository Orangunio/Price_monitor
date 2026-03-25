import sqlite3
import pandas as pd

def preview_data():
    conn = sqlite3.connect('Data/prices.db')
    # Pobieramy wszystko z tabeli
    df = pd.read_sql_query("SELECT * FROM price_history", conn)
    conn.close()
    
    print("--- PODGLĄD DANYCH W BAZIE ---")
    print(df.head()) # Pokazuje pierwsze 5 wierszy
    print(f"\nŁączna liczba rekordów: {len(df)}")

if __name__ == "__main__":
    preview_data()