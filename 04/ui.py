# ui.py
"""
Ievade/izvade funkciju modulis minēšanas spēlei.
"""

def display_start():
    """Sākuma ziņojums spēlētājam."""
    print("Spēle sākas. Esmu nolēmis slepeno skaitli no 1 līdz 100.")

def prompt_guess() -> int:
    """Ielūg ievadīt minējumu no lietotāja (1..100) ar validāciju."""
    while True:
        s = input("Jūsu minējums (1-100): ")
        try:
            g = int(s)
        except ValueError:
            print("Ievade nav skaitlis. Lūdzu, ievadi veselu skaitli no 1 līdz 100.")
            continue
        if 1 <= g <= 100:
            return g
        print("Nederīgs diapazons. Ievadi skaitli no 1 līdz 100.")

def display_feedback(result: str):
    """Parāda atsauksmi atkarībā no rezultāta."""
    if result == 'high':
        print("Par lielu!")
    elif result == 'low':
        print("Par mazu!")
    else:
        print("Apsveicu! Tu uzminēji slepeno skaitli.")

def ask_play_again() -> bool:
    """Jautā, vai spēlējam vēlreiz. Atgriež True/False."""
    again = input("Vai spēlējam vēlreiz? (j/n): ").strip().lower()
    return again == 'j'

def reveal_secret(secret: int):
    """Parāda slepeno skaitli (pēc zaudējuma)."""
    print(f"Pareizā atbilde bija: {secret}")

if __name__ == "__main__":
    display_start()
    guess = prompt_guess()
    print(f"Jūs ievadījāt: {guess}")
