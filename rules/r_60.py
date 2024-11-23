from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

# subclass of InterfaceEngine
class InterfaceEngine_60ans(InterfaceEngine):
    # a refaire
    @Rule(Cadeau(age="60plus"), Cadeau(interest="jardinage"))
    def cadeau_senior_jardinage(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Outils de jardin ergonomiques \n"
                                       "- Livres sur les plantes \n"
                                       "- Abonnement à un magazine de jardinage")))

    @Rule(Cadeau(age="60plus"), Cadeau(interest="confort"))
    def cadeau_senior_confort(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Coussin chauffant \n"
                                       "- Plaid doux \n"
                                       "- Pantoufles confortables")))