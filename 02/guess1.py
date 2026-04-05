# guess.py
# Vienkāršā spēle ar minēšanu, bez moduļiem (deterministiska slepenā vērtība)

# Ievads: spēle tiek spēlēta bez atsevišķa “do...while” cikla.
# Lielā mīnusa gadījumā: tiek piedāvāts spēlēt vēlreiz ārējais cikls.

# Slepenā vērtība (determinēta, jo bez moduļiem nav iespējams ģenerēt patiesi nejaušu skaitli)
SLEPENS_SK = 42  # vērtība no 1 līdz 100, var mainīt, ja nepieciešams

# Iesākumam spēle sākas ar uzvaru/neveiksmi
while True:
    print("Spēle sākas. Esmu nolēmis slepeno skaitli no 1 līdz 100.")
    slepenais = SLEPENS_SK
    mIdeas = 0  # mēģinājumu skaits
    uzmine = None

    # Spēles iekšējais cikls: mēģinājumi, beigsies, ja uzminēts vai būs 10 mēģinājumu
    while True:
        migi = input("Jūsu minējums (1-100): ")
        try:
            g = int(migi)
        except ValueError:
            # Nekorekts ievades gadījums – parāda paziņojumu, nekontrolē spēli
            print("Ievade nav skaitlis. Lūdzu, ievadi veselu skaitli no 1 līdz 100.")
            continue  # turpina spēli bez padarītiem mēģinājumiem
        if g < 1 or g > 100:
            print("Nederīgs diapazons. Ievadi skaitli no 1 līdz 100.")
            continue  # nekontrpret spēli, nekas nenotiek

        mIdeas += 1
        uzmine = g

        if uzmine > slepenais:
            print("Par lielu!")
        elif uzmine < slepenais:
            print("Par mazu!")
        else:
            print("Apsveicu! Tu uzminēji slepeno skaitli.")
            break  # uzvara

        # Ja ir izšķiroši daudz mēģinājumu bez uzminējuma
        if mIdeas >= 10:
            print(f"Tu neuzminēji slepeno skaitli pēc 10 mēģinājumiem.")
            print(f"Pareizā atbilde bija: {slepenais}")
            break

    # Spēle beigusies – jautā spēlēt vēlreiz
    again = input("Vai spēlējam vēlreiz? (j/n): ").strip().lower()
    if again != "j":
        print("Paldies par spēli!")
        break
