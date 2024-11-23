from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

# subclass of InterfaceEngine
class InterfaceEngine_13_17ans(InterfaceEngine):
    # a refaire
    @Rule(Cadeau(age="13-17ans"), Cadeau(interest="jeux_video"))
    def cadeau_adolescent_jeux_video(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Carte cadeau Steam \n"
                                       "- Manette de jeu \n"
                                       "- Abonnement à un service de jeux en ligne")))