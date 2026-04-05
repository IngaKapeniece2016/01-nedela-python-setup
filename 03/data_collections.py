#satur A daļu (saraksti), B daļu (vārdnīcas) un C daļu (kombinācijas) 
# data_collections.py
# Uzdevums: datu kolekcijas (lists un dict) demonstrācija
# A daļa: Saraksti (lists)
# B daļa: Vārdnīcas (dict)
# C daļa: Kombinācijas (list[dict])
# Piemēri tiek demonstrēti ar print izteikumiem, lai redzētu rezultātu konsolē.

def data_collections_demo():
    # 1) A daļa - saraksti
    # 1.1 Izveidojam sarakstu ar 5+ skaitļiem
    skaitli = [1, 2, 3, 4, 5]  # sākotnējais saraksts (5 elementi)

    # 1.2 Pievienojam vēl vienu elementu ar .append()
    skaitli.append(6)  # tagad saraksts: [1, 2, 3, 4, 5, 6]

    # 1.3 Dzēšana ar .pop() (parasti no beigām)
    izņemtais = skaitli.pop()  # izņemtais >= 6; atgriež 6; saraksts ir [1,2,3,4,5]

    # Teorētiski varam pretējā gadījumā izmantot .pop( indeks ) ja vajag konkrētu vietu
    # 1.4 Aprēķināsim summu un vidējo, izmantojot for ciklu (ne sum()/len())
    summa = 0
    skaitļu_skaits = 0
    for a in skaitli:
        summa += a
        skaitļu_skaits += 1

    vid = summa / skaitļu_skaits if skaitļu_skaits > 0 else 0

    # 1.5 Filtrēšana: no saraksta izveido jaunu sarakstu ar pāra skaitļiem
    paaraini = []
    for x in skaitli:
        if x % 2 == 0:
            paaraini.append(x)

    # 1.6 Demonstrē šķēlumu (slice)
    pirmie_3 = skaitli[:3]       # pirmie 3 elementi
    peedējie_2 = skaitli[-2:]     # pēdējie 2 elementi
    katrs_otrais = skaitli[::2]  # katrs otrais elements

    # 2) B daļa - vārdnīcas
    # 2.1 Izveidojam vārdnīcu ar 3+ studentiem
    studenti = {
        "Anna": 85,
        "Jānis": 72,
        "Līga": 95
    }

    # 2.2 Pievienojam jaunu studentu un atjaunojam esošu atzīmi
    studenti["Mārtiņš"] = 78
    studenti["Anna"] = 90  # atjaunošana

    # 2.3 Iterēšana ar .items()
    print("\n--- Vārdnīcas saturs ---")
    for name, grade in studenti.items():
        print(f"{name}: {grade}")

    # 2.4 Atrodam labāko studentu (augstāko atzīmi) - izmantojam for ciklu
    labākais_vards = None
    labaka_atzime = -1
    for name, grade in studenti.items():
        if grade > labaka_atzime:
            labaka_atzime = grade
            labākais_vards = name

    print(f"Labākais students: {labākais_vards} ({labaka_atzime})")

    # 3) C daļa - kombinācijas: saraksts ar vārdnīcām
    kombinacija = [
        {"name": "Anna", "grade": 85},
        {"name": "Jānis", "grade": 72},
        {"name": "Līga", "grade": 95}
    ]

    # 3.1 Filtrēšana: tikai studenti ar atzīmi >= 80
    students_80_plus = [s for s in kombinacija if s["grade"] >= 80]

    # 3.2 Izvade ar enumerate() un f-strings:
    print("\n--- Studenti ar atzīmi >= 80 ---")
    for idx, s in enumerate(students_80_plus, start=1):
        print(f"{idx}. {s['name']} — {s['grade']}")

    # 3.3 papildus demonstrācija (neobligāti): kā izvadīt vienā rindā
    # lauki = ", ".join([f"{s['name']}:{s['grade']}" for s in students_80_plus])
    # print("Saraksts:", lauki)

def main():
    data_collections_demo()

if __name__ == "__main__":
    main()
