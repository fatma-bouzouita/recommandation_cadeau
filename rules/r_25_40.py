from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

# subclass of InterfaceEngine
class InterfaceEngine_25_40ans(InterfaceEngine):
        # a refaire
    @Rule(Cadeau(age="25-40ans"), Cadeau(interest="cuisine"))
    def cadeau_adulte_cuisine(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Robot de cuisine \n"
                                       "- Cours de cuisine \n"
                                       "- Livre de recettes gastronomiques")))