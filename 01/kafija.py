# Programma: Kafijas iegāde veikalā
# Mērķis: Parādīt divus skaidrus algoritmus soli pa solim
# ar komentāriem, kā veikt kafijas iegādi veikalā.

def print_steps(title, steps):
    # Palīgfunkcija, kas izdara vienkāršu formatētu izvadīšanu:
    # - uzsāk ar virsrakstu
    # - katram solim pievieno numuru un soli teksta saturā
    print(title)
    for idx, step in enumerate(steps, start=1):
        print(f"{idx}. {step}")
    print()  # tukša rinda pēc algoritma

def main():
    # Algoritms 1: Kafijas izvēle un salīdzināšana veikalā
    # Šis algoritms ved lietotāju cauri kafijas izvēles procesam.
    alg1_steps = [
        "Ieeju veikalā un sagatavoju sarakstu ar gaumēm – domāju par stiprumu, maltuma veidu un izcelsmi.",
        "Aplūkoju kafijas plauktus un atlasu 3–5 variantus, ko vēlos salīdzināt tuvāk.",
        "Pārbaudu etiķeti: izcelsmi (valsts/reģions), grauzdējuma līmeni (light/medium/dark), maltuma veidu (veselas pupiņas/mlta), derīguma termiņu un iepakojuma tilpumu.",
        "Salīdzinu cenu par tilku un iespējamo daudzumu (piem., 250 g, 500 g, 1 kg); ņemu vērā arī kvalitātes marķējumus un no kurienes kafija nāk.",
        "Izvēlos vienu kafiju (vai divas dažādas) un noliek uz groza – pielāgoju pēc gaumes.",
        "Dodos uz kasi, lai turpinātu ar pirkumu un apmaksu."
    ]

    # Algoritms 2: Pirkuma pabeigšana un maksāšana
    alg2_steps = [
        "Eju uz kasi ar izvēlētajām precēm grozā.",
        "Pārbaudu grozu saturu un apstiprinu preču daudzumu un kopīgo summu.",
        "Izvēlos maksāšanas veidu (skaidru naudu vai karti).",
        "Ja maksāju ar karti: ievadu maksāšanas kartes datus vai izmantoju konta/biometrijas autentifikāciju, ja nepieciešams.",
        "Apstiprinu darījumu, saņemu kvīti vai maksājuma apstiprinājumu, un no maksāšanas termināļa saņemu pirkuma apliecinājumu.",
        "Paņemu iegādāto kafiju un iznāk no veikala."
    ]

    print_steps("Algoritms 1: Kafijas izvēle un salīdzināšana veikalā", alg1_steps)
    print_steps("Algoritms 2: Pirkuma pabeigšana un maksāšana", alg2_steps)

if __name__ == "__main__":
    main()
