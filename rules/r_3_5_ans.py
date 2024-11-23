from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

# subclass of InterfaceEngine
class InterfaceEngine_3_5ans(InterfaceEngine):
    # a refaire
    @Rule(Cadeau(age="3-5ans"), Cadeau(interest="dessin"))
    def cadeau_enfant_dessin(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Livres à colorier \n"
                                       "- Feutres lavables \n"
                                       "- Kit de dessin pour enfants")))

    @Rule(Cadeau(age="3-5ans"), Cadeau(interest="histoires"))
    def cadeau_enfant_histoires(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Livres illustrés \n"
                                       "- Marionnettes \n"
                                       "- Coffret d'histoires audio")))
