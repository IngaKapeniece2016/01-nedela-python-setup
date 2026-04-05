# game_logic.py
"""
Minēšanas spēles loģika (tīras funkcijas, bez I/O).
"""

MAX_TRIES = 10
SLEPENS_SK = 42  # determinēta slepenā vērtība; var mainīt

def generate_secret() -> int:
    """Atgriež slepeno skaitli (determinēta vērtība)."""
    return SLEPENS_SK

def check_guess(guess: int, secret: int) -> str:
    """
    Salīdzina minējumu ar slepeno skaitli.
    Atgriež 'low' (par zemu), 'high' (par augstu) vai 'correct' (pareizi).
    """
    if guess < secret:
        return 'low'
    if guess > secret:
        return 'high'
    return 'correct'

def is_game_over(tries: int, result: str) -> bool:
    """Pārbauda vai spēle beigusies (uzminēts vai trīsums izslēgts)."""
    return result == 'correct' or tries >= MAX_TRIES

if __name__ == "__main__":
    secret = generate_secret()
    print("Slepenais skaitlis (tests):", secret)
    print("check_guess(40, secret) ->", check_guess(40, secret))
    print("check_guess(42, secret) ->", check_guess(42, secret))
    print("is_game_over(10, 'low') ->", is_game_over(10, 'low'))
