import utils as utils

class FibreOptique:


    def init(self, distance, attenuation, epissures, perte_epissure, connecteurs, perte_connecteur):
        utils.valider_positifs(distance, attenuation, epissures, perte_epissure, connecteurs, perte_connecteur)
        self.distance = distance
        self.attenuation = attenuation
        self.epissures = epissures
        self.perte_epissure = perte_epissure
        self.connecteurs = connecteurs
        self.perte_connecteur = perte_connecteur



    def pertes_totales(self):
        return (
            self.distance * self.attenuation +
             self.epissures * self.perte_epissure +
            self.connecteurs * self.perte_connecteur
        )

    def rapport(self):
        return f"""
=== RAPPORT FIBRE OPTIQUE ===
Distance               : {self.distance} km
Atténuation            : {self.attenuation} dB/km
Épissures              : {self.epissures} × {self.perte_epissure} dB
Connecteurs            : {self.connecteurs} × {self.perte_connecteur} dB
------------------------------
PERTES TOTALES         : {self.pertes_totales():.2f} dB
"""
