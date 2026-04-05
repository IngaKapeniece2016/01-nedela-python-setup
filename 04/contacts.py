# kontakti.py
# Kontaktu pārvaldība ar JSON (load/save) un vienkāršs CLI: add, list, search
# Auto-izveide: contacts.json tukšam sarakstam

import json
import os
import argparse

def ensure_contacts_file(path='contacts.json'):
    """Izveido tukšu kontaktu saraksta failu, ja tas neeksistē."""
    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=2)
        print(f"Izveidots jauns fails: {path}")

def load_contacts(contacts_file='contacts.json'):
    """Ielādē kontaktus no JSON faila. Ja fails nav derīgs, atgriež tukšu sarakstu."""
    if not os.path.exists(contacts_file):
        return []
    with open(contacts_file, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_contacts(contacts, contacts_file='contacts.json'):
    """Saglabā kontakti sarakstu JSON failā."""
    with open(contacts_file, 'w', encoding='utf-8') as f:
        json.dump(contacts, f, ensure_ascii=False, indent=2)

def add_contact(contacts):
    """Pievieno jaunu kontaktu sarakstam, lūdz ievadi datus lietotājam."""
    name = input("ievadiet kontakta vārdu: ").strip()
    phone = input("ievadiet tālruņa nr.: ").strip()
    if not name:
        print("Konta vārds nedrīkst būt tukšs.")
        return False
    contacts.append({"name": name, "phone": phone})
    print(f"Kontakts '{name}' ir pievienots.")
    return True

def list_contacts(contacts):
    """Parāda visus kontaktiem sarakstu cilvēkam lasāmā formā."""
    if not contacts:
        print("Kontaktu nav šobrīd.")
        return
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c.get('name')} - {c.get('phone', '')}")

def search_contacts(contacts, query):
    """Meklē kontaktus pēc vārda vai telefona."""
    query = (query or '').lower()
    results = []
    for c in contacts:
        if query in c.get('name', '').lower() or query in c.get('phone', '').lower():
            results.append(c)
    return results

def main():
    # Auto-izveide tūlīt pēc programmas uzsākšanas
    ensure_contacts_file()

    parser = argparse.ArgumentParser(description='Kontaktu pārvaldība (JSON).')
    subparsers = parser.add_subparsers(dest='command')

    subparsers.add_parser('add', help='Pievienot jaunu kontaktu')
    subparsers.add_parser('list', help='Parādīt visus kontaktus')
    search_p = subparsers.add_parser('search', help='Meklēt kontaktā pēc vārda vai telefona')
    search_p.add_argument('query', nargs='?', default='', help='meklējamais teksts')

    args = parser.parse_args()

    contacts = load_contacts()

    if args.command == 'add':
        if add_contact(contacts):
            save_contacts(contacts)
    elif args.command == 'list':
        list_contacts(contacts)
    elif args.command == 'search':
        results = search_contacts(contacts, args.query)
        if results:
            for c in results:
                print(f"{c.get('name')} - {c.get('phone')}")
        else:
            print("Nav atrasti kontakti, kas atbilstēj query.")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
