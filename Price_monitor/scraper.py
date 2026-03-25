import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(filename='logs/pipeline.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_prices():
    url = "http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        products = []
        for item in soup.select('.product_pod'):
            name = item.select_one('h3 a')['title']
            price_raw = item.select_one('.price_color').text
            
            # --- TRANSFORMACJA ---
            # Czyszczenie ceny: "£51.77" -> 51.77
            price = float(price_raw.replace('£', ''))
            
            products.append({
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'product_name': name,
                'price': price,
                'store_name': 'BooksToScrape'
            })
            
        logging.info(f"Pomyślnie pobrano {len(products)} produktów.")
        return pd.DataFrame(products)

    except Exception as e:
        logging.error(f"Błąd podczas pobierania danych: {e}")
        return pd.DataFrame()