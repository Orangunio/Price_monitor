import sqlite3
import pandas as pd

DB_PATH = "Data/prices.db"

def init_db():
    """Tworzy tabelę, jeśli jeszcze nie istnieje."""
    conn = sqlite3.connect(DB_PATH)
    query = """
    CREATE TABLE IF NOT EXISTS price_history (
        timestamp TEXT,
        product_name TEXT,
        price REAL,
        store_name TEXT
    )
    """
    conn.execute(query)
    conn.close()

def save_to_db(df):
    """Zapisuje DataFrame do SQLite (tryb append)."""
    if df.empty:
        return
    conn = sqlite3.connect(DB_PATH)
    df.to_sql('price_history', conn, if_exists='append', index=False)
    conn.close()