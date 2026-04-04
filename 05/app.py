# app.py
# CLI Izdevumu izsekotājs: pievienot, apskatīt, dzēst, filtrēt pēc mēneša, kopsummas, eksportēt CSV
# Izmanto moduļus: storage.py, logic.py, export.py

from storage import load_expenses, save_expenses
from logic import filter_by_month, sum_total, sum_by_category, get_available_months
from export import export_to_csv
from datetime import datetime

# Iespējamās kategorijas; lietotājs var tās papildināt/dinamiski pievienot, ja nepieciešams
CATEGORIES = [
    "Ēdiens",
    "Transports",
    "Izklaide",
    "Komunālie maksājumi",
    "Veselība",
    "Iepirkšanās",
    "Cits",
]

EXPENSES_FILE_DEFAULT = "expenses.json"  # saglabāšanas fails (ja grib mainīt)

def show_menu():
    print("\nIzdevumu izsekotājs (CLI) – izvēlieties darbību:")
    print("1. Pievienot izdevumu")
    print("2. Apskatīt visus izdevumus")
    print("3. Dzēst izdevumu")
    print("4. Filtrēt pēc mēneša")
    print("5. Parādīt kopsummas pa kategorijām un kopējo sumu")
    print("6. Eksportēt CSV")
    print("7. Iestatīt mēneša budžetu")  # jauna opcija
    print("8. Beigt darbu")
    return input("Izvēlieties opciju (1-8): ").strip()

def input_float(prompt: str) -> float:
    """Palīgfunkcija ievadei dekadālijām (float)."""
    while True:
        val = input(prompt).strip()
        try:
            return float(val)
        except ValueError:
            print("Lūdzu ievadiet derīgu skaitli (piem., 12.50).")

def add_expense(expenses: list) -> None:
    """Pievieno jaunu izdevumu klāt esošajam sarakstam."""
    # Datums
    while True:
        date_str = input("Datums (YYYY-MM-DD): ").strip()
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Nederīgs datums. Lūdzu ievadiet formātā YYYY-MM-DD (piem., 2025-03-14).")

    # Summa
    amount = input_float("Summa (piem., 12.34): ")

    # Kategorija (iespējams pievienot arī jaunu, ja nav esošajā sarakstā)
    cat = input(f"Kategorija (esošās: {', '.join(CATEGORIES)}). Ja nepieciešams, ierakstiet jaunu: ").strip()
    if cat and cat not in CATEGORIES:
        # Pievienojam jaunu kategoriju lokāli; tas ļauj nākamajos mezglos izmantot
        CATEGORIES.append(cat)
        print(f"Jauna kategorija pievienota: {cat}")

    if not cat:
        cat = "Cits"

    desc = input("Apraksts (nav obligāti): ").strip()

    expense = {
        "date": date_str,
        "amount": amount,
        "category": cat,
        "description": desc
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Izdevums pievienots.")
    
# Pārbaudām budžetu
    check_budget_alert(expenses)
        
# --- Budžeta papildinājums ---
monthly_budget = {}  # glabā budžetu pa mēnešiem, formāts {"YYYY-MM": summa}

def set_monthly_budget():
    """Lietotājs var ievadīt budžeta limitu konkrētam mēnesim."""
    month = input("Ievadiet mēnesi budžetam (YYYY-MM): ").strip()
    try:
        year, m = map(int, month.split("-"))
        float(m)  # tikai validācija
    except Exception:
        print("Nederīgs formāts. Lieto YYYY-MM.")
        return
    amount = input_float("Ievadiet budžeta limitu šim mēnesim: ")
    monthly_budget[month] = amount
    print(f"Budžets {month} iestatīts: {amount:.2f}")

def check_budget_alert(expenses: list):
    """Pārbauda, vai konkrētā mēnesī izdevumi tuvojas budžetam."""
    if not monthly_budget:
        return  # nav budžeta
    # aprēķinām summu pa mēnešiem
    month_totals = {}
    for exp in expenses:
        m = exp["date"][:7]  # "YYYY-MM"
        month_totals[m] = month_totals.get(m, 0) + exp["amount"]
    # pārbaudām katru budžetu
    for month, limit in monthly_budget.items():
        spent = month_totals.get(month, 0)
        if spent >= limit:
            print(f"⚠️ BRĪDINĀJUMS! Izdevumi mēnesī {month} ({spent:.2f}) pārsniedz vai ir vienādi ar budžetu ({limit:.2f})")
        elif spent >= 0.8 * limit:
            print(f"⚠️ Brīdinājums: Tuvojas budžeta limits mēnesim {month} ({spent:.2f}/{limit:.2f})")
            
def list_expenses(expenses: list) -> None:
    """Parāda visus izdevumus rindā ar indeksu, lai ērtāk dzēšanai."""
    if not expenses:
        print("Nav neviena izdevuma.")
        return
    print(f"\n{'Nr':<4} {'Datums':<12} {'Summa':<10} {'Kategorija':<20} Apraksts")
    print("-" * 60)
    for i, exp in enumerate(expenses, start=1):
        date = exp.get("date", "")
        amount = f"{exp.get('amount', 0):.2f}"
        category = exp.get("category", "")
        description = exp.get("description", "")
        print(f"{i:<4} {date:<12} {amount:<10} {category:<20} {description}")

def delete_expense(expenses: list) -> None:
    """Izdzēš izvēlēto izdevumu pēc rindas numura."""
    if not expenses:
        print("Nav izdevumu dzēšanai.")
        return
    list_expenses(expenses)
    idx_str = input("Ievadiet rindas numuru, ko dzēst (vai atgriezties): ").strip()
    if not idx_str:
        return
    try:
        idx = int(idx_str)
        if 1 <= idx <= len(expenses):
            to_del = expenses[idx - 1]
            confirm = input(f"Vai tiešām dzēst izdevumu {idx} ({to_del['date']} {to_del['amount']:.2f} {to_del['category']})? (jā/nē): ").strip().lower()
            if confirm in ("ja", "jā", "yes", "y"):
                expenses.pop(idx - 1)
                save_expenses(expenses)
                print("Izdevums dzēsts.")
            else:
                print("Dzēšana atcelta.")
        else:
            print("Nederīga rindas numura vērtība.")
    except ValueError:
        print("Nederīga ievade.")

def filter_by_month_cli(expenses: list) -> None:
    """Filtrē izdevumus pēc izvēlēta mēneša un parāda tos."""
    months = get_available_months(expenses)
    if not months:
        print("Nav pieejamu mēnešu izvadīšanai.")
        return
    print(" pieejamie mēneši (YYYY-MM):")
    for m in months:
        print(f" - {m}")
    sel = input("Ievadiet mēnesi (YYYY-MM), kuru filtrēt: ").strip()
    if not sel:
        return
    try:
        year, month = map(int, sel.split("-"))
    except Exception:
        print("Nederīgs formāts. Lieto YYYY-MM.")
        return
    filtered = filter_by_month(expenses, year, month)
    print(f"\nIzdevumi mēnesī {sel}: {len(filtered)} vienības")
    list_expenses(filtered)

def show_summary_cli(expenses: list) -> None:
    """Parāda kopsummas pa kategorijām un kopējo summu."""
    if not expenses:
        print("Nav izdevumu, par kuriem rēķināt kopsummu.")
        return
    sums = sum_by_category(expenses)
    total = sum_total(expenses)
    print("\nKopsumma pa kategorijām:")
    for cat, val in sums.items():
        print(f" - {cat}: {val:.2f}")
    print(f"Kopējā summa: {total:.2f}")

def export_csv_cli(expenses: list) -> None:
    """Eksportē izdevumus uz CSV failu."""
    if not expenses:
        print("Nav izdevumu eksportēšanai.")
        return
    filepath = input("Ievadiet CSV faila ceļu (piem., expenses.csv): ").strip()
    if not filepath:
        print("Nederīgs ceļš.")
        return
    if not filepath.lower().endswith(".csv"):
        filepath += ".csv"
    export_to_csv(expenses, filepath)
    print(f"CSV eksportēts uz: {filepath}")

def main():
    # Ielādējam datus no JSON
    expenses = load_expenses()  # atgriež sarakstu (list)
    print("Sveicināti! Izdevumu izsekotājs CLI darbojas.")
    while True:
        choice = show_menu()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            list_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            filter_by_month_cli(expenses)
        elif choice == "5":
            show_summary_cli(expenses)
        elif choice == "6":
            export_csv_cli(expenses)
        elif choice == "7":
            set_monthly_budget()
        elif choice == "8":
            print("Paldies, aizveru programmu. Līdz nākamajai reizei!")
            break
        else:
            print("Nederīga izvēle. Lūdzu ievadiet numuru no 1 līdz 8.")

if __name__ == "__main__":
    main()
