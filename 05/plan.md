# Projekta plāns jeb Programmas apraksts
Izdevumu izsekošanas CLI rīka izveidošana, kas ļauj pievienot un pārvaldīt ikdienas izdevumus, grupēt pa kategorijām, skatīt mēneša kopsummas un eksportēt uz CSV. Dati saglabājas JSON starp sesijām.
## Mērķis
CLI programma, kas ļauj: pievienot izdevumus, apskatīt, dzēst, filtrēt pēc mēneša, redzēt kopsummu pa kategorijām, eksportēt CSV, saglabāt datus JSON starp sesijām.
B. Datu struktūra
expense_tracker/
├── app.py # Galvenā programma (izvēlne, lietotāja mijiedarbība)
├── storage.py # JSON failu operācijas
├── logic.py # Biznesa loģika (filtrēšana, grupēšana, summas)
├── export.py # CSV eksports
└── expenses.json # Dati (izveidojas automātiski)
docs/
├── DEVLOG.md # Izstrādes žurnāls
└── plan.md # Sākotnējais plāns (1. soļa rezultāts)
└── README.md # Projekta dokumentācija
• Viens izdevuma ieraksts izskatās šādi:
{
    "date": "2026-04-04",
    "amount": 13.69,
    "category": "Ēdiens",
    "description": "pelmeņi"
  }
• Es izvēlējos tieši šādu struktūru, jo ērti pārskatāma bez liekā.
C. Moduļu plāns
• Projektā būs 4 faili: app.py, kurš darbina logic.py (filtrēšana, kopsummas, grupēšana pa kategorijām), storage.py (saglabā informāciju, ielāde un saglabāšana JSON failā) un export.py (eksportē izdevumus uz CSV failu ar csv.writer()). 
• Kuras funkcijas būs katrā failā? (nosaukumi un īsi apraksti)
storage.py būs load_expenses (nolasa izdevumu sarakstu no JSON faila.
    Atgriež sarakstu (list) ar izdevumu ierakstiem.
    Ja fails neeksistē vai ir kļūda ar saturu, atgriež tukšu sarakstu []), 
    save_expenses (Saglabā izdevumu sarakstu JSON failā ar UTF-8 encodējumu.  Saglabāšana notiek ar indentēšanu, lai fails būtu viegli lasāms)
logic.py būs filter_by_month (atgriež izdevumus, kuru datums pieder norādītajam mēnesim);
sum_total (aprēķina kopējo izdevumu summu no sniegtā saraksta);
sum_by_category (Izveido kopsummu pa kategorijām);
get_available_months (Atgriež unikālo mēnešu sarakstu).
export.py būs export_to_csv (Eksportē izdevumus uz CSV failu)
app.py būs palīgfunkcija input_float (nosaka, vai pareizs skaitlis ievadīts) ; add_expense (Pievieno jaunu izdevumu klāt esošajam sarakstam) ; list_expenses (Parāda visus izdevumus rindā ar indeksu, lai ērtāk dzēšanai) ; delete_expense (Izdzēš izvēlēto izdevumu pēc rindas numura) ; filter_by_month_cli (Filtrē izdevumus pēc izvēlēta mēneša un parāda tos) ; show_summary_cli (Parāda kopsummas pa kategorijām un kopējo summu) ; export_csv_cli (Eksportē izdevumus uz CSV failu) ; main() (Ielādējam datus no JSON expenses = load_expenses()  # atgriež sarakstu (list)).
Datu struktūra  jeb moduļu sadalījums: (1) app.py: galvenā CLI interfeisa loģika un lietotāja mijiedarbība (2) storage.py: datu uzglabāšana/ielāde (JSON) (3) logic.py: biznesa loģika (filtrēšana, grupēšana, kopsummas); (4) export.py: CSV eksports; (5) README.md, plāna dokuments plan.md, kā arī plūsmas diagrammas.
D. Lietotāja scenāriji
Lietotājs ievada nepareizu skaitli izdevumu izsekotājam, kur jāievada viens līdz 7, ievada 8, tad tiek dota otra iespēja ievadīt pareizu skaitli bez liekiem print.
Lietotājs ievada nepareizi datumu (norādīts pareizais ievades formāts Datums (YYYY-MM-DD)), programma parāda kļūdas paziņojumu un ļauj mēģināt
vēlreiz, konkretizējot datuma ievadi "Nederīgs datums. Lūdzu ievadiet formātā YYYY-MM-DD (piem., 2025-03-14)."
E. Robežgadījumi
• Kas notiek, ja expenses.json neeksistē? 
funkcija load_expenses nolasa izdevumu sarakstu no JSON faila.   Atgriež sarakstu (list) ar izdevumu ierakstiem.Ja fails neeksistē vai ir kļūda ar saturu, atgriež tukšu sarakstu [].
Kas notiek, ja lietotājs ievada negatīvu summu? 
Kas notiek, ja lietotājs ievada tukšu aprakstu? 
to programma pieļauj, jo šis lauks nav obligāts, uz ko programma norāda "Apraksts (nav obligāti)".
Kas notiek, ja lietotājs ievada nepareizu datumu?
Lietotājs ievada nepareizi datumu (norādīts pareizais ievades formāts Datums (YYYY-MM-DD)), programma parāda kļūdas paziņojumu un ļauj mēģināt
vēlreiz, konkretizējot datuma ievadi "Nederīgs datums. Lūdzu ievadiet formātā YYYY-MM-DD (piem., 2025-03-14)."
Kas notiek, ja saraksts ir tukšs un lietotājs izvēlas "Parādīt"?
Lietotājam tiek izvadīts "Nav neviena izdevuma." un ļauts vēlreiz izvēlēties izdevumu izsekotāja darbību 1-7.
## Uzdevumi
[1] Idejas izdomāšana
[2] Programmēšana
[3] Testēšana
[4] publicēšana GitHub repozitorijā
## Termiņi
- 1. diena: plānošana
- 2.–5. diena: izstrāde
## Piezīmes
Darbs izstrādāts patstāvīgi, meklējot nezināmo čatbotos un pieejamajā literatūrā.
Datu formāts: expenses.json, datuma formāts YYYY-MM-DD, katram ierakstam lauki: date, amount, category, description (datums, summa, kategorija, apraksts)
Izmantojam datetime un csv Python standarta bibliotēkas.