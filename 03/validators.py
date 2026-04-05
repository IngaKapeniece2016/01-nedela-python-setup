#Lietotājs var importēt validators.py ārpus uzdevuma (is_email, is_phone_number, is_valid_age, is_strong_password, is_valid_date).
#Iekļautie main testi nodrošina demonstrācijas un pašaiztestēšanas iespēju, kā tika pieprasīts MI formulējumā.
#Funkcijas ir tīras (nav print iekšpusē) un atgriež tikai bool.
# -*- coding: utf-8 -*-
"""
3. nedēļas uzdevums: Validācijas bibliotēka
Funkcijas atgriež bool (True/False) un ir gatavas importēšanai nākamajās nedēļās.
Katrai funkcijai ir docstring ar mērķi, parametriem un atgriežamo vērtību.

Funkcijas:
- is_email(text): vienkārša e-pasta validācija
- is_phone_number(text): Latvijas formāts +371 XXXXXXXX (ar vai bez atstarpēm)
- is_valid_age(age): vecums 0–150 (int vai iespējams konvertēt uz int)
- is_strong_password(text): vismaz 8 simboli, satur burtus un ciparus
- is_valid_date(text): formāts YYYY-MM-DD ar īsto datumu
"""

import re
from datetime import datetime

def is_email(text: str) -> bool:
    """Pārbauda, vai ievadā ir vienkārša e-pasta adrese ar formu lietotājs@domēns.tld.
    Prasības:
    - satur vienu '@'
    - pirms un pēc '@' ir kāda rakstzīme
    - domēna daļā ir punkts un kāds tūris (domēns.tld)
    Args:
        text: ievades virkne
    Returns:
        bool: True, ja formāts atbilst vismaz šiem nosacījumiem
    Example:
        is_email("anna@inbox.lv") -> True
        is_email("anna@") -> False
    """
    if not isinstance(text, str):
        return False
    text = text.strip()
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(pattern, text) is not None

def is_phone_number(text: str) -> bool:
    """Latvijas numurs formātā +371 XXXXXXXX (8 cipari), ar vai bez atstarpēm.
    Varianti: "+371 12345678" vai "+37112345678"
    Args:
        text: ievades virkne
    Returns:
        bool: True, ja forma atbilst
    Example:
        is_phone_number("+371 26123456") -> True
        is_phone_number("26123456") -> False
    """
    if not isinstance(text, str):
        return False
    text = text.strip()
    pattern = r"^\+371\s?\d{8}$"
    return re.match(pattern, text) is not None

def is_valid_age(age) -> bool:
    """Validē vecumu kā veselīgu skaitli no 0 līdz 150.
    Args:
        age: jebkurš ievades veids (skaitlis vai skaitļa reprezentācija)
    Returns:
        bool: True, ja vecums ir diapazonā [0, 150]
    """
    try:
        n = int(age)
    except (TypeError, ValueError):
        return False
    return 0 <= n <= 150

def is_strong_password(text: str) -> bool:
    """Pārbauda, vai parole ir pietiekami droša: vismaz 8 simboli, satur burtus un ciparus.
    Args:
        text: parole kā virkne
    Returns:
        bool: True, ja parole atbilst kritērijiem
    """
    if not isinstance(text, str):
        return False
    if len(text) < 8:
        return False
    has_digit = any(ch.isdigit() for ch in text)
    has_alpha = any(ch.isalpha() for ch in text)
    return has_digit and has_alpha

def is_valid_date(text) -> bool:
    """Pamatvalidācija datuma formātā YYYY-MM-DD ar faktiskā datuma pārbaudi.
    Args:
        text: ievades virkne
    Returns:
        bool: True, ja datums ir pareizs un formāts derīgs
    """
    if not isinstance(text, str):
        return False
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    print("Testi: is_email")
    print("anna@inbox.lv ->", is_email("anna@inbox.lv"))  # True
    print("anna@ ->", is_email("anna@"))                  # False
    print("anna@inbox ->", is_email("anna@inbox"))        # False
    print()

    print("Testi: is_phone_number")
    for s in ["+371 26123456", "+37126123456", "26123456"]:
        print(f"{s} -> {is_phone_number(s)}")
    print()

    print("Testi: is_valid_age")
    for v in [25, -1, "30", "abc"]:
        print(f"{v} -> {is_valid_age(v)}")
    print()

    print("Testi: is_strong_password")
    tests = ["password", "passw0rd", "12345678", "Abc12345"]
    for t in tests:
        print(f"'{t}' -> {is_strong_password(t)}")
    print()

    print("Testi: is_valid_date")
    dates = ["2024-12-31", "2024-02-30", "2025-01-01", "2023-13-01"]
    for d in dates:
        print(f"'{d}' -> {is_valid_date(d)}")
