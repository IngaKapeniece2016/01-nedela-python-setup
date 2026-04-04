# export.py
# CSV eksports: eksportēest izdevumus uz CSV failu ar csv.writer()
# encoding utf-8-sig nodrošina BOM, lai Excel to pareizi atvērtu

import csv
from typing import List, Dict, Any


def export_to_csv(expenses: List[Dict[str, Any]], filepath: str) -> None:
    """Eksportē izdevumus uz CSV failu.

    Args:
        expenses: Saraksts ar izdevumu ierakstiem.
        filepath: Ceļš uz CSV fails, kurš tiks izveidots/updated.
    """
    with open(filepath, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        # Virsraksti CSV kolonnām
        writer.writerow(["Datums", "Summa", "Kategorija", "Apraksts"])
        for expense in expenses:
            writer.writerow([
                expense.get("date"),
                f"{expense.get('amount', 0):.2f}",
                expense.get("category"),
                expense.get("description", "")
            ])
