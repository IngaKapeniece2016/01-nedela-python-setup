# storage.py
# Datu uzglabāšana: ielāde un saglabāšana JSON failā
# Izmantojam UTF-8 encodēšanu un 2 līmeņu formatēšanu (indent=2) lasāmībai.

import json
import os
from typing import List, Dict, Any

FILENAME = "expenses.json"  # Galvenais datu failiņš, kurā glabājam izdevumu sarakstu


def load_expenses() -> List[Dict[str, Any]]:
    """Nolasa izdevumu sarakstu no JSON faila.
    Atgriež sarakstu (list) ar izdevumu ierakstiem.
    Ja fails neeksistē vai ir kļūda ar saturu, atgriež tukšu sarakstu [].
    """
    if not os.path.exists(FILENAME):
        # Ja faila nav, atgriež tukšu sarakstu, lai programma var turpināt darbību
        return []
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Drošības pārbaude: ja tas nav saraksts, atgriež tukšu sarakstu
            if isinstance(data, list):
                return data
            return []
    except json.JSONDecodeError:
        # Ja fails ir korumpēts vai nav derīgs JSON, atgriež tukšu sarakstu
        return []
    except Exception:
        # Papildu aizsardzība pret vispārējām kļūdām
        return []


def save_expenses(expenses: List[Dict[str, Any]]) -> None:
    """Saglabā izdevumu sarakstu JSON failā ar UTF-8 encodējumu.
    Saglabāšana notiek ar indentēšanu, lai failu būtu viegli lasāms.
    """
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)
