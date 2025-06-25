def valider_positifs(*args):
    for val in args:
        if not isinstance(val, (int, float)) or val < 0:
            raise ValueError(f"Valeur invalide : {val}")

def demander_valeur(label, type_attendu=float):
    while True:
        try:
            valeur = type_attendu(input(f"{label} : "))
            if valeur < 0:
                raise ValueError
            return valeur
        except:
            print("Entrée invalide. Veuillez entrer une valeur numérique positive.")