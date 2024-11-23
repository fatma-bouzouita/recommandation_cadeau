from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

# subclass of InterfaceEngine
class InterfaceEngine_18_24ans(InterfaceEngine):
    # a refaire
    @Rule(Cadeau(age="18-24ans"), Cadeau(interest="voyage"))
    def cadeau_jeune_adulte_voyage(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Sac à dos de voyage \n"
                                       "- Carnet de voyage \n"
                                       "- Appareil photo instantané")))


