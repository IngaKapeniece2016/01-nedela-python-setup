1. nedēļa — Pašrefleksijas jautājumi 

Atbildi uz šiem jautājumiem saviem vārdiem. Mērķis nav “pareiza atbilde” — mērķis ir pārliecināties, ka tu saproti, ko esi iemācījies. Ja kādā punktā jūties nedrošs — tas ir signāls, ka jāpiestrādā. 

Iesniedz šo dokumentu kopā ar pārējo mājasdarbu. 

Koncepti 

Kas ir programma? Kā tu to izskaidrotu cilvēkam, kurš nekad nav programmējis? 
Programma komandas datoram vai citai ierīcei, kas tai liek paveikt noteiktas darbības. Programmas pamatā ir algoritms, kas rakstīts konkrētā programmēšanas valodā.

Kas ir algoritms? Kā tas atšķiras no vienkāršas instrukcijas? Algoritms ir precīzas un nemainīgā secībā noteiktas darbības. Instrukcijas ir vadlīnijas, kuras parāda drošu ceļu uz rezultātu, tomēr atstāj vietu atkāpēm. Algoritms sastāv no koda, to saprot dators, kurā ir, piemēram, instalēts PYTHON un to spēj dators izpildīt, secīgi izdarot tur aprakstīto. Instrukcija nav algoritms, dators to nesaprot un nespēj secīgi izpildīt.

Kādas trīs īpašības padara algoritmu derīgu (valid)? Pastāsti katru saviem vārdiem un dod piemēru, kas šo īpašību pārkāpj. 
1. Algoritmam ir sākums, noslēgums un nobeigums, secīgi soļi, tas ir nostrādāts un neuzkaras, tas spēj atkārtoties bez kļūdām un katru reizi sniegt iepriekš paredzēto iznākumu. 2. Algoritms ir derīgs, ja to ir iespējams izpildīt. Validitāte (derīgums) ir pārkāpta, ja, piemēram, algoritms nestartējas. 3. Python algoritms ir derīgs priekš Python programmas, ne C++, tur jau cits kods, cita programmēšanas valoda. 

Ko nozīmē “secīga izpilde” (sequential execution)? Kāpēc datoram ir svarīgi, kādā secībā soļi tiek izpildīti? 
Noteiktās darbībās secībai ir nozīme, jo nav iespējams veikt nākošās darbības, kamēr nav pabeigtas iepriekšējās; nav notikusi  resursa sagatavošana nākamām darbībām. Programmā tiek sakārtoti soļi secīgā kārtībā, loģiskajos soļos, lai varētu izpildīt uzdevumu tā, kā tas domāts. 

Izskaidro modeli “ievade → apstrāde → izvade” ar vienu konkrētu piemēru no ikdienas vai no sava mājasdarba.  
Ievades dati ir mainīgie dati, ko katrā reizē varam ievadīt, ko prasa programma, lai varētu katrreiz izvadīt mums vēlamo rezultātu. Piemēram, ievadi savu vārdu(ievade), programma apstrādā (dota komanda izprintēt Hello, tad vārdu, tad atlikušo teikumu) un izvada "Hello, Mārtiņ, esmu gatavs darbam!" 

Kas ir interpretators (interpreter) un ko tas dara ar tavu Python kodu? 
Interpretators ir programma, kas nolasa un izpilda tavu Python kodu soli pa solim: nolasa kodu, pārbauda sintaksi, izpilda komandas.

Kāda ir procesora (CPU) un atmiņas (memory) loma programmas izpildē? Izskaidro vienkāršoti, saviem vārdiem. 
Atmiņa glabā datus, procesors izpilda komandss. CPU-centrālais procesors. 

Kas notiek, ja tavā kodā ir sintakses kļūda? Kāpēc programma netiek izpildīta pat daļēji? 
Jo kodam jābūt precīzam, rezultāts ir precīzs. Dators dara tieši to, ko mēs liekam, nepiedomā klāt. 

Praktiskie darbi 

Vai Python ir veiksmīgi uzstādīts tavā datorā? Kādu Python versiju parāda python --version? 
Pyhtons ir veiksmīgi uzstādīts. Uzrāda versiju 3.14.3 

Vai tu spēj palaist kodu no termināļa vai IDE? Apraksti, kā tu to dari — kādus soļus veic.  
Spēju no cmd, Visual Studio Code un Windows Powershell. Ierakstu meklēšanas laukā cmd, atveru melno ekrānu, ierakstu python, tad kodu, palaižu.

Vai tu spēj izveidot .py failu un to izpildīt? Kas notiek, ja mēģini palaist failu, kura nav?  
Jā, esmu izveidojusi daudz .py failu un izpildījusi. Atver Visual Studio Code, New file, ieraksta faila nosaukumu+.py un sāk rakstīt kodu. Palaiž ar run. Nav sanācis palaist failu, kura nav.

Vai tu uzrakstīji un palaidi savu “Hello, world!” programmu? Kas tieši parādījās ekrānā? 
Jā, parādījās uzraksts "Hello, world!"

Vai tu veiksmīgi nomainīji izvades tekstu? Ko tu mainīji un kāds bija rezultāts? 
Mainīju uz tekstu vairākos variantos ar vairākām rindiņām. Ir vismaz trīs veidi, kā to izdarīt, pievienotajā prinscreen redzams rezultāts, visi trīs veidi izdevās.
 

Refleksija 

Kāpēc programmētājam ir jābūt precīzam katrā instrukcijā? Ko dators nevar “uzminēt”? 
Dators nav cilvēks un nevar uzminēt, ka kods ir nepareizs, esi pārrakstījies. Piem., meklējot failu pēc nosaukuma, tas neatradīs failu, ja tā nosaukums būs ievadīts kļūdaini. 

Kāpēc precizitāte ir svarīga programmās? Apraksti vienu situāciju, kur neliela neprecizitāte varētu radīt lielu problēmu. 
Precizitāte ir svarīga, jo dators izpilda tieši un tikai to, ko tam liek.

04.04.2026.g. 