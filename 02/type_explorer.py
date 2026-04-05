# type_explorer.py
# Mērķis: demonstrēt Python datu tipus, to uzvedību un vienkāršas konversijas.
# Saturs:
#  - piešķirt vismaz 2 pamata tipu vērtības (str, int, float, bool, None)
#  - konsoles izvade ar type() tipu nosaukumiem
#  - vismaz 3 Truthy / Falsy gadījumi ar komentāriem
#  - vismaz 3 tiešas datu tipu konversijas (explicit conversions) ar robežgadījumiem
# Piezīme: programma darbojas bez ārējiem moduļiem (neizmanto import).

# 1) Pamattipu piesaistes mainīgajiem
# Šeit piešķiram vismaz divas (šajā piemērā vairāk) pamata tipu vērtības.

sateksts = "Sveiki, Python!"  # str tipa vērtība (virkne)
skaitlis_int = 42            # int tipa vērtība (vesels skaitlis)
skaitlis_float = 3.14159      # float tipa vērtība (daļskaitlis)
patiesiba = True               # bool tips (patiesība)
nav_definets = None             # None tipa vērtība (nav objekta)

# 2) Izvade ar tipa nosaukumu (type()) katrai vērtībai
print("2) Tipu informācija par ievadītajām vērtībām:")
print(f"Vērtība: {sateksts!r}, Tips: {type(sateksts).__name__}")      # skaļā virkne
print(f"Vērtība: {skaitlis_int!r}, Tips: {type(skaitlis_int).__name__}")  # int
print(f"Vērtība: {skaitlis_float!r}, Tips: {type(skaitlis_float).__name__}")  # float
print(f"Vērtība: {patiesiba!r}, Tips: {type(patiesiba).__name__}")       # bool
print(f"Vērtība: {nav_definets!r}, Tips: {type(nav_definets).__name__}") # NoneType
print()  # tukša rinda grozāmībai

# 3) Vismaz 3 Truthy / Falsy uzvedības piemēri (komentāros paskaidrojumi)
print("3) Truthy / Falsy demonstrācija:")

# Tukša virkne ir False
print("bool(\"\") ->", bool(""))  # False

# Netukša virkne ir True (pat ja satur vārdu '0')
print("bool(\"0\") ->", bool("0"))  # True

# Atstarpes vienmēr padara virkni par netukšu mācību piemēru; tukšā vietā joprojām ir vairāka rakstzīmes
print("bool(\" \") ->", bool(" "))  # True (virkne nav tukša)

# Nulle (0) ir False
print("bool(0) ->", bool(0))  # False

# Tukšs saraksts ir False
print("bool([]) ->", bool([]))  # False

# None ir False
print("bool(None) ->", bool(None))  # False

# True un False kā skaitliskas vērtības (bool ir int apakšklase)
print("True + True ->", True + True)  # 2

# Īsi piemēri ar "jaukto aritmētiku" (bools kā skaitļi)
print("True * 10 ->", True * 10)  # 10
print("False + 5 ->", False + 5)  # 5
print("10 / True ->", 10 / True)  # 10.0
print()  # tukša rinda

# 4) Tiešās (explicit) datu tipu konversijas (ar robežgadījumiem)
print("4) Tiešas konversijas (explicit conversions):")

# 4.1 Pārveidot virkni uz int (ja virkne satur skaitli)
print("int('5') ->", int("5"))  # 5
print("int('5') + 3 ->", int("5") + 3)  # 8

# 4.2 Robežgadījums: mēģinot konvertēt virkni, kas nav skaitlis
try:
    int("abc")
except ValueError:
    print("int('abc') -> ValueError: nevar konvertēt virkni uz int")

# 4.3 Pārveide no virtenes uz float
print("float('3.14') ->", float("3.14"))  # 3.14

# 4.4 Pārveide no virknes ar eksponentu notāciju uz float
print("float('1e3') ->", float("1e3"))  # 1000.0

# 4.5 Pārveide no float uz int (robežgadījums: nepārvērš uzapaļošanu)
print("int(3.99) ->", int(3.99))  # 3

# 4.6 Pārveide no bool uz int/float (bool ir int apakšklase)
print("int(True) ->", int(True))    # 1
print("float(False) ->", float(False))  # 0.0

# 4.7 Robežgadījums: int('5.0') nav derīgs uz int (ValueError)
try:
    int("5.0")
except ValueError:
    print("int('5.0') -> ValueError: nevar konvertēt uz int tieši no '5.0'")

# 4.8 Piemērs ar int(float(...)) (precizitāte)
print("int(float('3.14')) ->", int(float("3.14")))  # 3

print()  # beigu tukšā rinda
