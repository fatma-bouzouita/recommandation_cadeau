from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

# subclass of InterfaceEngine
class InterfaceEngine_6_9ans(InterfaceEngine):
    # a refaire
    @Rule(Cadeau(age="6-9ans"), Cadeau(interest="jeux_de_construction"))
    def cadeau_enfant_construction(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Lego \n"
                                       "- Meccano \n"
                                       "- Puzzles 3D")))

    @Rule(Cadeau(age="6-9ans"), Cadeau(interest="sport"))
    def cadeau_enfant_sport(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Ballon de football \n"
                                       "- Trottinette \n"
                                       "- Mini-table de ping-pong")))