import os
from scraper import fetch_prices
from db_manager import init_db, save_to_db

def run_pipeline():
    # 1. Przygotowanie infrastruktury (foldery)
    os.makedirs('data', exist_ok=True)
    os.makedirs('logs', exist_ok=True)
    
    print("Inicjalizacja bazy danych...")
    init_db()
    
    # 2. Extract & Transform
    print("Pobieranie danych...")
    df = fetch_prices()
    
    # 3. Load
    if not df.empty:
        print(f"Ładowanie {len(df)} rekordów do bazy...")
        save_to_db(df)
        print("Gotowe!")
    else:
        print("Pipeline zakończony - brak nowych danych.")

if __name__ == "__main__":
    run_pipeline()