# fizzbuzz.py
# Vienkāršā fizzbuzz versija bez moduļiem
# Ievads: lietotājs ievada N caur input()
# Izvade: 1..N ar atsevišķiem vārdiem FizzBuzz, sadalīti ar komatiem
# Piemērs (ievade): 15
# Izvade: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz

# 1) Ievadi N un pārbaudi, vai tas ir derīgs pozitīvs vesels skaitlis
try:
    raw = input("Ievadi N (pozitīvs vesels skaitlis): ")
    N = int(raw)
    if N < 1:
        print("Kļūda: N jābūt pozitīvam veselam skaitlim.")
        raise SystemExit(1)
except ValueError:
    print("Kļūda: N nav derīgs skaitlis.")
    raise SystemExit(1)

# 2) Veido izvadi kā sarakstu, kur katrs elements ir vienkāršs virkne (string)
parts = []
for i in range(1, N + 1):
    # Vispirms pārbauda lielāko dalāmību (FizzBuzz)
    if i % 15 == 0:
        parts.append("FizzBuzz")
    # Tad atsevišķi: Fizz (dalās ar 3)
    elif i % 3 == 0:
        parts.append("Fizz")
    # Tad: Buzz (dalās ar 5)
    elif i % 5 == 0:
        parts.append("Buzz")
    else:
        parts.append(str(i))

# 3) Izdod visu rindā ar komatu un atstarpēm
print(", ".join(parts))
