#Izmanto random moduli.
#Spēle izvēlas slepeno skaitli no 1 līdz 100 un aicina lietotāju to uzminēt.
#Pievienots vienkāršs mēģinājumu skaitītājs un žurnāls par katru minējumu.
#Pēc uzminēšanas jautājums par spēles turpināšanu (j/n).
# guess.py
# Vienkārša minēšanas spēle ar nejaušu slepeno skaitli 1..100.
# Izmanto random moduli (random.randint) slepenā skaitļa ģenerēšanai.
# Spēlei ir ārējais cikls, lai iespējotu atkārtotu spēli pēc uzvarēšanas.

import random  # modulis nejaušai skaitļu ģenerēšanai

print("Sveicināti spēlē! Es uzminēšu slepeno skaitli no 1 līdz 100.")

while True:
    # Slepenā skaitļa ģenerēšana katrai spēles kārtai
    slepenais = random.randint(1, 100)
    mēģinājumu_skaits = 0

    while True:
        ievade = input("Ievadi savu minējumu (1-100): ").strip()
        try:
            minējums = int(ievade)
        except ValueError:
            print("Ievade nav skaitlis. Lūdzu ievadi veselu skaitli no 1 līdz 100.")
            continue

        if minējums < 1 or minējums > 100:
            print("Nederīgs diapazons. Ievadi skaitli no 1 līdz 100.")
            continue

        mēģinājumu_skaits += 1

        if minējums < slepenais:
            print("Par mazu!")
        elif minējums > slepenais:
            print("Par lielu!")
        else:
            print(f"Apsveicu! Tu uzminēji slepeno skaitli {slepenais} ar {mēģinājumu_skaits} mēģinājumiem.")
            break  # uzvara šajā kārtā

    # Jautājums, vai spēlēt vēlreiz
    atkartot = input("Vai spēlējam vēlreiz? (j/n): ").strip().lower()
    if atkartot != "j":
        print("Paldies par spēli!")
        break
