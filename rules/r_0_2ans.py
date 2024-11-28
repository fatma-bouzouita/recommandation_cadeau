from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

#subclass of InterfaceEngine
class InterfaceEngine_0_2ans(InterfaceEngine):
    #garcon------------------------------------------------------------------------------------------------------------------
    @Rule(Cadeau(age="0-2ans",sexe="masculin",occasion="naissance"))
    def cadeau_naissance_garcon(self):
        self.declare(Resultat(result=(
            "Pour une naissance (garçon), voici des idées de cadeaux : \n"
            "- Ensemble de vêtements pour nouveau-né (ex : grenouillère à motifs) \n"
            "- Jouet d'éveil interactif (ex : hochets en forme de voitures ou animaux) \n"
            "- Mobile avec des couleurs et formes vives pour le berceau \n"
            "- Coffret souvenir personnalisé (ex : boîte à souvenirs, bracelet gravé) \n"
            "- Couverture douce et confortable aux motifs animaliers."
        )))

    @Rule(Cadeau(age="0-2ans",sexe="masculin",occasion="anniversaire"))
    def cadeau_anniversaire_garcon(self):
        self.declare(Resultat(result=(
            "Pour un anniversaire (garçon), voici des idées : \n"
            "- Voiture ou train en bois adaptés aux tout-petits \n"
            "- Puzzle ou jeux de construction simples \n"
            "- Tapis d'éveil ou de jeu interactif \n"
            "- Livre avec des personnages ou animaux à toucher \n"
            "- Peluches thématiques (ex : dinosaure, super-héros) \n"
            "- Veilleuse colorée en forme de fusée ou étoile."
            "- Ensemble de vêtements thématiques (ex : super-héros ou animaux)."
        )))
        
    @Rule(Cadeau(age="0-2ans"), Cadeau(sexe="masculin"))
    def cadeau_bebe_garcon(self):
        self.declare(Resultat(result=(
            "Pour un garçon de 0-2 ans, vous pouvez offrir : \n"
            "- Jouets d'éveil adaptés à son âge (ex : cubes empilables, puzzles simples) \n"
            "- Livres interactifs ou sonores \n"
            "- Tapis de jeu coloré \n"
            "- Peluches ou jouets thématiques (voitures, animaux)."
            "- Ensemble de vêtements adaptés à la saison \n"
            "- Veilleuses avec musique apaisante \n"
            )))

    #fille------------------------------------------------------------------------------------------------------------------
    @Rule(Cadeau(age="0-2ans",sexe="feminine",occasion="naissance"))
    def cadeau_naissance_fille(self):
        self.declare(Resultat(result=(
        "Pour une naissance (fille), voici des idées de cadeaux : \n"
        "- Robe ou ensemble de vêtements avec des motifs doux (ex : fleurs, étoiles) \n"
        "- Poupée ou peluche en tissu hypoallergénique \n"
        "- Bracelet de naissance ou boîte à bijoux personnalisée \n"
        "- Mobile musical en couleurs pastel pour le berceau \n"
        "- Couverture douce personnalisée avec le prénom."
        )))

    @Rule(Cadeau(age="0-2ans",sexe="feminine",occasion="anniversaire"))
    def cadeau_anniversaire_fille(self):
            self.declare(Resultat(result=(
            "Pour un anniversaire (fille), voici des idées : \n"
            "- Poupées interactives ou peluches thématiques (ex : licornes, princesses) \n"
            "- Livres d'éveil colorés avec textures (ex : livres en tissu ou en plastique) \n"
            "- Tapis d'éveil musical ou en forme de fleurs \n"
            "- Jouets d'éveil éducatifs (ex : cubes avec formes géométriques) \n"
            "- Ensemble d'accessoires mignons (ex : bandeaux, chaussettes colorées)."
            "- Tapis de jeu décoratif ou musical \n"
            )))

    @Rule(Cadeau(age="0-2ans",sexe="feminine"))
    def cadeau_bebe_fille(self):
            self.declare(Resultat(result=(
            "Pour une fille de 0-2 ans, vous pouvez offrir : \n"
            "- Jouets interactifs avec textures et couleurs vives \n"
            "- Peluches ou poupées adaptées à son âge \n"
            "- Robes ou ensembles de vêtements doux \n"
            "- Jouets sensoriels d'éveil (ex : jouets en silicone, anneaux de dentition) \n"
            "- Couverture douce personnalisée \n"
            "- Livres avec textures et illustrations colorées \n"
            "- Veilleuses en forme d'animaux ou avec lumière douce."
            )))
