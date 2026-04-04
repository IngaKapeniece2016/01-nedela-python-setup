# logic.py
# Biznesa loģika: filtrēšana, kopsummas, grupēšana pa kategorijām.
# Šeit nav neviena tieša darbība ar IO; funkcijas ir tīras (pure functions).

from datetime import datetime
from typing import List, Dict, Any


def filter_by_month(expenses: List[Dict[str, Any]], year: int, month: int) -> List[Dict[str, Any]]:
    """Atgriež izdevumus, kuru datums pieder norādītajam mēnesim.

    Args:
        expenses: Saraksts ar izdevumu ierakstiem (katrs ir dict ar atbilstošiem laukiem).
        year: Gads kā vesels skaitlis (piemēram 2025).
        month: Mēnesis kā vesels skaitlis (1-12).

    Returns:
        Saraksts ar izdevumiem, kuru datums ir norādītajā mēnesī.
    """
    result: List[Dict[str, Any]] = []
    for expense in expenses:
        d = datetime.strptime(expense["date"], "%Y-%m-%d")
        if d.year == year and d.month == month:
            result.append(expense)
    return result


def sum_total(expenses: List[Dict[str, Any]]) -> float:
    """Aprēķina kopējo izdevumu summu no sniegtā saraksta.

    Args:
        expenses: Saraksts ar izdevumu ierakstiem.

    Returns:
        Kopējā summa (apaļota uz 2 zīmēm aiz komata).
    """
    total = sum(expense.get("amount", 0) for expense in expenses)
    return round(total, 2)


def sum_by_category(expenses: List[Dict[str, Any]]) -> Dict[str, float]:
    """Izveido kopsummu pa kategorijām.

    Args:
        expenses: Saraksts ar izdevumu ierakstiem.

    Returns:
        Dict ar formātu {kategorija: summa}.
    """
    totals: Dict[str, float] = {}
    for expense in expenses:
        cat = expense.get("category", "Cits")
        totals[cat] = totals.get(cat, 0) + expense.get("amount", 0)
    # Apkope to 2 decimālie cipari
    return {cat: round(total, 2) for cat, total in totals.items()}


def get_available_months(expenses: List[Dict[str, Any]]) -> List[str]:
    """Atgriež unikālo mēnešu sarakstu kā 'YYYY-MM', kā sorted secība.

    Args:
        expenses: Saraksts ar izdevumu ierakstiem.

    Returns:
        Lote ar 'YYYY-MM' formāta mēnešiem, sakārtoti augošā secībā.
    """
    months = set()
    for expense in expenses:
        d = datetime.strptime(expense["date"], "%Y-%m-%d")
        months.add((d.year, d.month))
    sorted_months = sorted(months)
    return [f"{year:04d}-{month:02d}" for year, month in sorted_months]
