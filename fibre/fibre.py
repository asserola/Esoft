from fibre.calcul import FibreOptique

def saisir_float(message):
    while True:
        valeur = input(message)
        try:
            return float(valeur)
        except ValueError:
            print("⛔ Entrée invalide. Veuillez entrer un nombre.")

def saisir_int(message):
    while True:
        valeur = input(message)
        try:
            return int(valeur)
        except ValueError:
            print("⛔ Entrée invalide. Veuillez entrer un entier.")

while True:
    # Saisie sécurisée
    distance = saisir_float("Distance (km) : ")
    attenuation = saisir_float("Atténuation (dB/km) : ")
    epissures = saisir_int("Nombre d'épissures : ")
    perte_epissure = saisir_float("Perte par épissure (dB) : ")
    connecteurs = saisir_int("Nombre de connecteurs : ")
    perte_connecteur = saisir_float("Perte par connecteur (dB) : ")

    fibre = FibreOptique(distance, attenuation, epissures, perte_epissure, connecteurs, perte_connecteur)
    print(f"\n✅ Pertes totales : {fibre.calculer_pertes():.2f} dB\n")

    # Continuer ?
    if input("Faire un autre calcul ? (o/n) : ").strip().lower() != "o":
        print("👋 Fin.")
        break