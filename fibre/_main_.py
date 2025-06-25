from fibre.calcul import FibreOptique
from fibre.utils import demander_valeur

def main():
    print("=== CALCULATEUR DE PERTE FIBRE OPTIQUE ===")
    fibre = FibreOptique(
        distance=demander_valeur("Distance (km)"),
        attenuation=demander_valeur("Atténuation (dB/km)"),
        epissures=demander_valeur("Nombre d'épissures", int),
        perte_epissure=demander_valeur("Perte par épissure (dB)"),
        connecteurs=demander_valeur("Nombre de connecteurs", int),
        perte_connecteur=demander_valeur("Perte par connecteur (dB)")
    )
    print(fibre.rapport())
