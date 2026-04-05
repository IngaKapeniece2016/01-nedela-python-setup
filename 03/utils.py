# -*- coding: utf-8 -*-
"""
3. nedēļa — Utilītu bibliotēka
Funkciju komplekts ar docstringiem, tipa pārliecība un robežgadījumu pārbaudes.

Uzdevums:
- 8+ funkcijas: virknes, skaitļi, saraksti
- Docstring ar mērķi, parametriem, atgriežamo vērtību un piemēru
- Veselīgs pieeja ar noklusējuma parametriem (vismaz 2 funkcijām)
- Tīras funkcijas (bez blakusefektiem), ievaddatu validācija (piem., factorial(-1) -> ValueError)
- Demonstrācijas izsaukumi izpildes beigās (if __name__ == "__main__":)

Docstring piemērs ir iekļauts katrai funkcijai.
"""
from typing import Any, List
import math

# 1) virkņu funkcijas
def capitalize(text: str) -> str:
    """Pārvērš pirmās teksta virknes lielo burtu.
    Args:
        text: ievades virkne
    Returns:
        str: ar lielo sākumburtu, pārējais paliek nemainīts
    Example:
        >>> capitalize("hello")
        'Hello'
    """
    if not text:
        return text
    return text[:1].upper() + text[1:]

def truncate(text: str, max_len: int = 20) -> str:
    """Pārvērš virknēņu garumu uz ierobežotu garumu.
    Ja virkne ir garāka than max_len, tiek pievienots "..."
    Args:
        text: ievades virkne
        max_len: maksimālais garums atgrieztajā virknē
    Returns:
        str: īsāka vai vienāda garuma virkne
    Example:
        >>> truncate("abcdefg", max_len=5)
        'ab...'
    """
    if text is None:
        return ""
    if len(text) <= max_len:
        return text
    # aizņemam vietu lietotāja definētajam truncētajam "…" ar 3 punktiem
    cut = max_len - 3
    if cut < 0:
        cut = 0
    return text[:cut] + "..."

# 2) skaitļu funkcijas
def clamp(num: float, low: float, high: float) -> float:
    """Ierobežo skaitli diapazonā [low, high].
    Args:
        num: skaitlis, ko ierobežot
        low: zemākā robeža
        high: augšējā robeža
    Returns:
        float: ierobežotā vērtība
    Example:
        >>> clamp(15, 0, 10)
        10
        >>> clamp(-5, 0, 10)
        0
    """
    return max(low, min(num, high))

def is_prime(num: int) -> bool:
    """Pārbauda, vai skaitlis ir pirmskaitlis.
    Args:
        num: skaitlis, kuru pārbaudīt
    Returns:
        bool: True, ja pirmskaitlis, pretējā gadījumā False
    """
    if not isinstance(num, int) or num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0:
        return False
    limit = int(math.sqrt(num))  # robeža dalītājiem
    i = 3
    while i <= limit:
        if num % i == 0:
            return False
        i += 2
    return True

def factorial(n: int) -> int:
    """Raksta skaitļa n! (faktoriāls).
    Validācija: n >= 0, pretējā gadījumā izmet ValueError.
    Args:
        n: non-negatīvs vesels skaitlis
    Returns:
        int: n!
    Raises:
        ValueError: ja n < 0
    Example:
        >>> factorial(5)
        120
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n jābūt veselam skaitlim lielākam vai vienādam ar 0.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 3) sarakstu funkcijas
def total(numbers: List[float]) -> float:
    """Aprēķina skaitļu kopumu, izmantojot pamatloģiku (for cilpa).
    Args:
        numbers: skaitļu saraksts
    Returns:
        float: summa
    """
    total_val = 0
    for x in numbers:
        total_val += x
    return total_val

def average(numbers: List[float]) -> float:
    """Aprēķina vidējo aritmētisko.
    Nelieto sum() un len() (lai demonstrētu nojausmu par mehānismu).
    Args:
        numbers: skaitļu saraksts
    Returns:
        float: vidējais, ja nav elementu — 0.0
    """
    if not numbers:
        return 0.0
    total_val = 0
    count = 0
    for x in numbers:
        total_val += x
        count += 1
    return total_val / count if count else 0.0

# Papildus funkcija ar default parametru (divas funkcijas ar noklusējuma parametriem)
def repeat_text(text: str, times: int = 2) -> str:
    """Atgriež teksta atkārtojumu noteiktā skaitā reižu.
    Args:
        text: ievades virkne
        times: cik reizes atkārtot
    Returns:
        str: atkārtotā virkne
    """
    if times <= 0:
        return ""
    return text * times

if __name__ == "__main__":
    print("Demo: capitalize, truncate, clamp, is_prime, factorial, total/average, repeat_text")
    s = capitalize("hello world")
    print("Cap:", s)

    t = truncate("Šis ir ilgāks teksts un tiks saīsināts.", max_len=20)
    print("Trunc:", t)

    print("Clamp 15->", clamp(15, 0, 10), "| clamp -5->", clamp(-5, 0, 10))

    print("Is_prime 17:", is_prime(17), "Is_prime 18:", is_prime(18))

    print("factorial(5):", factorial(5))

    nums = [1, 2, 3, 4, 5]
    print("Total:", total(nums), "Average:", average(nums))

    print("Repeat:", repeat_text("A", times=3))
