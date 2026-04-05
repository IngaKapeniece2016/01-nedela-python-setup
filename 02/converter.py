#Mērķis: implementēt divvirzienu konversijas starp dažādām vienībām, izmantojot konstanšu nosaukumus ar lielajiem burtiem. Liekot lietotājam izvēlēties konversiju tipu, virzienu un ievadīt vērtību; izvadīt ar formatējumu {:.2f}.
#Definu konvertēšanas koeficientus kā konstantes (liels burts ar skaidru nosaukumu).
#Izdaru funkcijas konvertēt uz priekšu un atpakaļ katrai konversijai (km<->mi, kg<->lb, L<->gal).
#Izveidoju vienkāršu interaktīvu izvēlni ar input(), pārbaudu ievadi un aprēķinu.
#Izvade ir ar 2 decimāļu precizitāti, izmantojot f-strings.
#Pārbaudu ievadi, lai novērstu programmas avāriju uz nederīgiem skaitļiem.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 2 nedēļa MI: converter.py
# Konvertētāju interaktīva programma ar konstanšu izmantošanu.

# Konvertēšanas koeficienti (konstantes, lielie burti)
KM_TO_MI = 0.621371
MI_TO_KM = 1.0 / KM_TO_MI

KG_TO_LB = 2.20462
LB_TO_KG = 1.0 / KG_TO_LB

L_TO_GAL = 0.264172
GAL_TO_L = 1.0 / L_TO_GAL

USD_TO_EUR = 0.84235020
EUR_TO_USD = 1.0 / USD_TO_EUR

def convert_km_mi(value, to_miles=True):
    if to_miles:
        return value * KM_TO_MI
    else:
        return value * MI_TO_KM

def convert_kg_lb(value, to_pounds=True):
    if to_pounds:
        return value * KG_TO_LB
    else:
        return value * LB_TO_KG

def convert_l_gal(value, to_gal=True):
    if to_gal:
        return value * L_TO_GAL
    else:
        return value * GAL_TO_L

def convert_usd_eur(value, to_eur=True):
    if to_eur:
        return value * USD_TO_EUR
    else:
        return value * EUR_TO_USD

def ask_float(prompt):
    while True:
        s = input(prompt).strip()
        try:
            return float(s)
        except ValueError:
            print("Ievade nav skaitlis. Lūdzu ievadi derīgu skaitli.")

def main():
    print("Izvēlies konversiju:")
    print("1) km <-> mi")
    print("2) kg <-> lb")
    print("3) L <-> gal")
    print("4) $ <-> EUR")
    choice = input("> ").strip()
    if choice not in {"1","2","3","4"}:
        print("Nederīga izvēle.")
        return

    choice = int(choice)

    if choice == 1:
        print("Virziens: 1) km -> mi  2) mi -> km")
        dir_in = input("> ").strip()
        if dir_in not in {"1","2"}:
            print("Nederīga virziena izvēle.")
            return
        dir_in = int(dir_in)
        val = ask_float("Ievadi vērtību: ")
        if dir_in == 1:
            res = convert_km_mi(val, to_miles=True)
            print(f"{val:.2f} km = {res:.2f} mi")
        else:
            res = convert_km_mi(val, to_miles=False)
            print(f"{val:.2f} mi = {res:.2f} km")

    elif choice == 2:
        print("Virziens: 1) kg -> lb  2) lb -> kg")
        dir_in = input("> ").strip()
        if dir_in not in {"1","2"}:
            print("Nederīga virziena izvēle.")
            return
        dir_in = int(dir_in)
        val = ask_float("Ievadi vērtību: ")
        if dir_in == 1:
            res = convert_kg_lb(val, to_pounds=True)
            print(f"{val:.2f} kg = {res:.2f} lb")
        else:
            res = convert_kg_lb(val, to_pounds=False)
            print(f"{val:.2f} lb = {res:.2f} kg")

    elif choice == 3:
        print("Virziens: 1) L -> gal  2) gal -> L")
        dir_in = input("> ").strip()
        if dir_in not in {"1","2"}:
            print("Nederīga virziena izvēle.")
            return
        dir_in = int(dir_in)
        val = ask_float("Ievadi vērtību: ")
        if dir_in == 1:
            res = convert_l_gal(val, to_gal=True)
            print(f"{val:.2f} L = {res:.2f} gal")
        else:
            res = convert_l_gal(val, to_gal=False)
            print(f"{val:.2f} gal = {res:.2f} L")

    else:  # choice == 4
        print("Virziens: 1) USD -> EUR  2) EUR -> USD")
        dir_in = input("> ").strip()
        if dir_in not in {"1","2"}:
            print("Nederīga virziena izvēle.")
            return
        dir_in = int(dir_in)
        val = ask_float("Ievadi vērtību: ")
        if dir_in == 1:
            res = convert_usd_eur(val, to_eur=True)
            print(f"${val:.2f} USD = €{res:.2f} EUR")
        else:
            res = convert_usd_eur(val, to_eur=False)
            print(f"€{val:.2f} EUR = ${res:.2f} USD")

if __name__ == "__main__":
    main()
