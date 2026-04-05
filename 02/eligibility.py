#Mērķis: praktizēt nosacījumus ar and/or/not, izvadīt vairākas atbilstības vienlaicīgi un apstrādāt robežgadījumus (nepareiza ievade, negatīvs vecums).
#Ievaddatu validācija: vecums caur int(), kļūdu gadījumā piedāvā atkārtot ievadi; j/n reizes tiek konvertēti uz bool.
#Izveidoju loģiku četrām atbilstībām: balsot, auto īre, senioru atlaide, studentu atlaide.
#Attēloju rezultātus, izmantojot f-strings un latviskās atbilžu zīmes (Jā/Nē).
#Robežgadījumi tiek apstrādāti – negatīvs vecums vai jebkura nederīga ievade tiek pieslēgta pateicoties atkārtotai ievadei.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2 nedēļa MI: eligibility.py
# Nosaka dažādas atbilstības (balsošana, auto īre, senioru/studentu atlaides).

def parse_yes_no(prompt):
    """Atgriež bool (True ja 'j', False ja 'n'). Lieko ievadi atkārto līdz pareizam."""
    while True:
        ans = input(prompt).strip().lower()
        if ans in {'j', 'n'}:
            return ans == 'j'
        else:
            print("Lūdzu atbildiet ar 'j' (jā) vai 'n' (nav).")

def valid_age():
    """Iedod vecumu kā veselus gadus ar validāciju."""
    while True:
        s = input("Ievadi vecumu: ").strip()
        try:
            v = int(s)
            if v < 0:
                print("Vecums nevar būt negatīvs. Mēģini vēlreiz.")
                continue
            return v
        except ValueError:
            print("Ievade nav skaitlis. Lūdzu ievadi veselīgu vecumu.")

def main():
    print("Pārliecināsimies par atbilstību dažādiem gadījumiem.")
    age = valid_age()
    has_license = parse_yes_no("Vai ir autovadītāja apliecība? (j/n): ")
    is_student = parse_yes_no("Vai esi students? (j/n): ")
    is_veteran = parse_yes_no("Vai esi veterāns? (j/n): ")

    can_vote = age >= 18
    can_rent = (age >= 21) and has_license
    senior_discount = (age >= 65) or is_veteran
    student_discount = (16 <= age <= 26) and is_student

    print("---")
    print(f"Balsošana:        {'Jā' if can_vote else 'Nē'} ✓" if can_vote else f"Balsošana:        Nē ✗")
    print(f"Auto īre:         {'Jā' if can_rent else 'Nē'} ✗" if can_rent else f"Auto īre:         Nē ✗")
    print(f"Senioru atlaide:   {'Jā' if senior_discount else 'Nē'}" + (" ✓" if senior_discount else " ✗"))
    print(f"Studentu atlaide:  {'Jā' if student_discount else 'Nē'}" + (" ✓" if student_discount else " ✗"))

if __name__ == "__main__":
    main()
