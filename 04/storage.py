# storage.py
# Iepirkumu saraksta un cenu datu glabāšana ar JSON failiem
# Auto-izveide: shopping.json ([]), prices.json ({})

import json
import os

def ensure_json_file(path, initial_content):
    """Palīgfunkcija, lai izveidotu JSON failu ar inicialo saturu, ja tas neeksistē."""
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(initial_content, f, ensure_ascii=False, indent=2)

def ensure_storage_files():
    """Nodrošina, ka nepieciešamie JSON faili pastāv ar sākotnējo saturu."""
    ensure_json_file('shopping.json', [])
    ensure_json_file('prices.json', {})

def load_list(list_file='shopping.json'):
    """Ielādē iepirkumu sarakstu no JSON faila. Ja nav faila - atgriež tukšu sarakstu."""
    if not os.path.exists(list_file):
        return []
    with open(list_file, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_list(items, list_file='shopping.json'):
    """Saglabā iepirkumu sarakstu JSON failā."""
    with open(list_file, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

def load_prices(prices_file='prices.json'):
    """Ielādē cenas no JSON faila (nosaukums -> cena)."""
    if not os.path.exists(prices_file):
        return {}
    with open(prices_file, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_prices(prices, prices_file='prices.json'):
    """Saglabā cenas JSON failā."""
    with open(prices_file, 'w', encoding='utf-8') as f:
        json.dump(prices, f, ensure_ascii=False, indent=2)

def get_price(name, prices=None, prices_file='prices.json'):
    """Atgriež cenas vērtību priekš dotā nosaukuma, ja tā ir pieejama."""
    if prices is None:
        prices = load_prices(prices_file)
    return prices.get(name)

def set_price(name, price, prices=None, prices_file='prices.json'):
    """Iestata cenas vērtību nosaukumam un saglabā to failā."""
    if prices is None:
        prices = load_prices(prices_file)
    prices[name] = price
    save_prices(prices, prices_file)
ensure_storage_files()
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def ensure_json_file(path, initial_content):
    full_path = os.path.join(BASE_DIR, path)
    if not os.path.exists(full_path):
        with open(full_path, 'w', encoding='utf-8') as f:
            json.dump(initial_content, f, ensure_ascii=False, indent=2)
