# shop.py
# Iepirkumu saraksta CLI ar pamata I/O un aprēķiniem
# Izmanto storage.py un utils.py
# Komandas: add, list, total, clear

import storage

storage.ensure_storage_files()

import argparse
from storage import load_list, save_list, load_prices, save_prices, get_price, ensure_storage_files
from utils import calc_line_total, calc_grand_total, count_units

def add_item():
    """Pievieno jaunu preču sarakstam. Ja cena nav norādīta - mēģina to ielādēt no cenām datubāzē."""
    items = load_list()

    name = input("Ievadiet preces nosaukumu: ").strip()
    if not name:
        print("Preces nosaukums nedrīkst būt tukšs.")
        return

    qty_str = input("Ievadiet daudzumu (skaitli): ").strip()
    try:
        quantity = int(qty_str)
    except ValueError:
        quantity = 1

    price_input = input("Ievadiet cenu par vienību (EUR) - atstāj tukšu, ja nezinat: ").strip()
    price = None
    if price_input:
        try:
            price = float(price_input)
        except ValueError:
            price = 0.0

    if price is None:
        price = get_price(name) or 0.0

    items.append({"name": name, "quantity": quantity, "price": price})
    save_list(items)
    print(f"Pievienota: {name}, daudzums={quantity}, cena={price:.2f} EUR")

def list_items():
    items = load_list()
    if not items:
        print("Iepirkumu saraksts ir tukšs.")
        return
    print("Iepirkumu saraksts:")
    for i, it in enumerate(items, start=1):
        price = it.get('price', 0.0)
        qty = it.get('quantity', 0)
        line_total = calc_line_total(it)
        print(f"{i}. {it['name']}: daudzums={qty}, cena={price:.2f} EUR, līnijas summa={line_total:.2f} EUR")

def show_total():
    items = load_list()
    total = calc_grand_total(items)
    print(f"Kopējā summa: {total:.2f} EUR")

def clear_list():
    save_list([])
    print("Iepirkumu saraksts iztīrīts.")

def main():
    # Auto-izveide
    ensure_storage_files()

    parser = argparse.ArgumentParser(description='Iepirkumu saraksta pārvaldība (JSON).')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('add', help='Pievienot preces')
    subparsers.add_parser('list', help='Parādīt preces')
    subparsers.add_parser('total', help='Parādīt kopējo summu')
    subparsers.add_parser('clear', help='Iztīrīt sarakstu')

    args = parser.parse_args()

    if args.command == 'add':
        add_item()
    elif args.command == 'list':
        list_items()
    elif args.command == 'total':
        show_total()
    elif args.command == 'clear':
        clear_list()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
