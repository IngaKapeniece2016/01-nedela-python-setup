#izmanto sys.argv, ja ir
#citādi prasa input()
# FizzBuzz programma (darbojas gan ar sys.argv, gan ar input())

import sys

# Funkcija FizzBuzz loģikai
def fizzbuzz(N):
    rezultats = []

    for i in range(1, N + 1):

        # Vispirms pārbaudām dalāmību ar abiem
        if i % 3 == 0 and i % 5 == 0:
            rezultats.append("FizzBuzz")

        # Tad ar 3
        elif i % 3 == 0:
            rezultats.append("Fizz")

        # Tad ar 5
        elif i % 5 == 0:
            rezultats.append("Buzz")

        # Citādi – pats skaitlis
        else:
            rezultats.append(str(i))

    print(", ".join(rezultats))


# =========================
# GALVENĀ PROGRAMMAS DAĻA
# =========================

# Ja ir komandrindas arguments → izmantojam to
if len(sys.argv) > 1:
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("Kļūda: N nav skaitlis")
        sys.exit()
else:
    # Ja nav argumenta → prasām ievadi (strādā ar Run ▶)
    try:
        N = int(input("Ievadi skaitli N: "))
    except ValueError:
        print("Kļūda: jāievada skaitlis!")
        sys.exit()

# Pārbaudām, vai N ir pozitīvs
if N < 1:
    print("Kļūda: N jābūt pozitīvam veselam skaitlim")
    sys.exit()

# Izsaucam funkciju
fizzbuzz(N)