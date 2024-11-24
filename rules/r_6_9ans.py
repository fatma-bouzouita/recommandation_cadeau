from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

# subclass of InterfaceEngine
class InterfaceEngine_6_9ans(InterfaceEngine):
    #fille------------------------------------------------------------------------------------------------------------------
    #anniversaire
    @Rule(Cadeau(age="6-9ans", sexe="feminine", interest="jeux_de_construction", occasion="anniversaire"))
    def fille_anniversaire_construction(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Lego \n"
                                        "- Puzzles 3D\n"
                                        "- Kit de bricolage pour construire des bijoux ou accessoires\n"
                                        "- Jeu de mosaïques à assembler (ex. Quercetti Pixel Art)\n"
                                        "- Kapla\n"
                                        "- Jeux de construction magnétique (Magformers, Geomag)")))

    @Rule(Cadeau(age="6-9ans", sexe="feminine", interest="livres", occasion="anniversaire"))
    def fille_anniversaire_livre(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Une collection de contes classiques illustrés \n"
                                        "- Une série de livres d'aventures pour enfants (ex. \"La Cabane Magique\") \n"
                                        "- Un livre interactif avec activités ou autocollants \n"
                                        "- Un carnet d'histoires personnalisable où elle peut écrire ses propres histoires \n"
                                        "- Une bande dessinée ou un roman graphique adapté à son âge (ex. \"Les Sisters\", \"Mortelle Adèle\")")))

    @Rule(Cadeau(age="6-9ans", sexe="feminine", interest="sport", occasion="anniversaire"))
    def fille_anniversaire_sport(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Un kit de gymnastique ou de danse (tapis, rubans, chaussons) \n"
                                        "- Une corde à sauter colorée ou un jeu de fitness pour enfants \n"
                                        "- Un vélo ou une trottinette avec accessoires (casque, panier) \n"
                                        "- Un ballon adapté à son sport préféré (ex. football, basket, volleyball) \n"
                                        "- Une raquette et des volants pour jouer au badminton")))

    @Rule(Cadeau(age="6-9ans", sexe="feminine", interest="activités_artistiques", occasion="anniversaire"))
    def fille_anniversaire_art(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Un kit de peinture avec chevalet, pinceaux et aquarelles \n"
                                        "- Un coffret de création de bijoux (perles, fils, breloques) \n"
                                        "- Un livre ou un kit de coloriage géant avec des feutres et crayons \n"
                                        "- Un set de pâte à modeler ou de sculpture pour créer des formes artistiques \n"
                                        "- Un kit de broderie ou de couture simple pour débutants")))

    #fille-------------------------------------------------------------------------------------------------------------------
    #Récompense scolaire
    @Rule(Cadeau(age="6-9ans", sexe="feminine", interest="jeux_de_construction", occasion="récompense_scolaire"))
    def fille_recompense_construction(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Un coffret Lego Friends ou Lego Disney \n"
                                        "- Un kit Meccano pour créer des modèles amusants \n"
                                        "- Puzzles 3D\n"
                                        "- Kit de bricolage pour construire des bijoux ou accessoires\n"
                                        "- Un jeu de construction STEM pour apprendre en s'amusant \n"
                                        "- Un ensemble de blocs de construction en bois colorés")))

    @Rule(Cadeau(age="6-9ans", sexe="feminine", interest="livres", occasion="récompense_scolaire"))
    def fille_recompense_livre(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Un livre de science ludique pour enfants \n"
                                        "- Une bande dessinée adaptée à son âge (ex. Mortelle Adèle, Les Sisters) \n"
                                        "- Une lampe de lecture design pour l'encourager à lire le soir \n"
                                        "- Un livre sur des héroïnes inspirantes et leurs histoires \n"
                                        "- Un carnet personnalisé pour écrire ses propres histoires \n"
                                        "- Un abonnement à un magazine éducatif pour enfants")))

    @Rule(Cadeau(age="6-9ans", sexe="feminine", interest="sport", occasion="récompense_scolaire"))
    def fille_recompense_sport(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Des patins à roulettes ou un skateboard pour débutants \n"
                                        "- Une tenue de sport personnalisée avec son prénom \n"
                                        "- Un sac de sport pratique pour transporter ses affaires \n"
                                        "- Une montre connectée adaptée pour enfants pour suivre son activité \n"
                                        "- Un abonnement à un cours de sport ou à une activité en club \n"
                                        "- Un kit de frisbee ou de jeu d’extérieur interactif \n"
                                        "- Une raquette et des volants pour jouer au badminton")))

    @Rule(Cadeau(age="6-9ans", sexe="feminine", interest="activités_artistiques", occasion="récompense_scolaire"))
    def fille_recompense_art(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Un set pour créer des mosaïques ou des mandalas \n"
                                        "- Une imprimante pour photos ou designs créatifs à décorer \n"
                                        "- Un kit de fabrication de bougies ou de savons faits maison \n"
                                        "- Un coffret de création de bijoux (perles, fils, breloques) \n"
                                        "- Un carnet de croquis personnalisé et de qualité \n"
                                        "- Un set de pâte à modeler ou de sculpture pour créer des formes artistiques \n"
                                        "- Un kit de broderie ou de couture simple pour débutants")))

    #garcon------------------------------------------------------------------------------------------------------------------
    #anniversaire
    @Rule(Cadeau(age="6-9ans", sexe="masculin", interest="jeux_de_construction", occasion="anniversaire"))
    def garcon_anniversaire_construction(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Lego Technic pour construire des véhicules avancés \n"
                                        "- Un coffret Playmobil avec thème d’aventure ou d’exploration \n"
                                        "- Puzzles 3D\n"
                                        "- Meccano \n"
                                        "- Un jeu de construction électrique ou électronique pour introduire des circuits simples \n"
                                        "- Kapla\n"
                                        "- Jeux de construction magnétique (Magformers, Geomag)")))

    @Rule(Cadeau(age="6-9ans", sexe="masculin", interest="livres", occasion="anniversaire"))
    def garcon_anniversaire_livre(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Une collection de livres d'aventures comme Le Club des Cinq ou Les aventures de Tintin \n"
                                        "- Une série de livres d'aventures pour enfants (ex. \"La Cabane Magique\") \n"
                                        "- Un livre interactif avec des activités ou des pop-ups \n"
                                        "- Une bande dessinée humoristique ou d'action comme Astérix, Lucky Luke, ou Spirou \n"
                                        "- Un coffret de livres thématiques (super-héros, magie, mythologie, etc.)")))

    @Rule(Cadeau(age="6-9ans", sexe="masculin", interest="sport", occasion="anniversaire"))
    def garcon_anniversaire_sport(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Un kit de mini-buts ou un panier de basketball portable \n"
                                        "- Une trottinette ou un skateboard avec des protections (casque, genouillères) \n"
                                        "- Un set de frisbee ou de jeu de lancer d'anneaux \n"
                                        "- Un ballon adapté à son sport préféré (ex. football, basket, volleyball) \n"
                                        "- Des vêtements ou accessoires de sport personnalisés (maillot de son équipe favorite, gourde, sac de sport) \n"
                                        "- Un trampoline de jardin pour s'amuser tout en faisant de l'exercice")))

    @Rule(Cadeau(age="6-9ans", sexe="masculin", interest="activités_artistiques", occasion="anniversaire"))
    def garcon_anniversaire_art(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Un kit de création de BD \n"
                                        "- Une boîte à outils pour des projets artistiques (colle, ciseaux, papiers colorés, paillettes) \n"
                                        "- Un livre ou un kit de coloriage géant avec des feutres et crayons \n"
                                        "- Un set de pâte à modeler ou de sculpture pour créer des formes artistiques \n"
                                        "- Un kit de construction créatif comme des mosaïques à assembler ou des perles à repasser")))

    #garcon------------------------------------------------------------------------------------------------------------------
    #Récompense scolaire
    @Rule(Cadeau(age="6-9ans", sexe="masculin", interest="jeux_de_construction", occasion="récompense_scolaire"))
    def garcon_recompense_construction(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Un set Lego thématique (voitures, super-héros, espace, etc.) \n"
                                        "- Une boîte K'NEX pour créer des machines en mouvement \n"
                                        "- Puzzles 3D\n"
                                        "- Des blocs de bois ou en plastique pour construire des structures libres \n"
                                        "- Un jeu de construction STEM pour apprendre en s'amusant \n"
                                        "- Un set de rails de train à assembler avec des accessoires interactifs.")))

    @Rule(Cadeau(age="6-9ans", sexe="masculin", interest="livres", occasion="récompense_scolaire"))
    def garcon_recompense_livre(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Un livre de science ludique pour enfants \n"
                                        "- Un livre sur les héros historiques ou des anecdotes fascinantes."
                                        "- Une lampe de lecture design pour l'encourager à lire le soir \n"
                                        "- Un livre sur les dinosaures ou les animaux, avec des images interactives \n"
                                        "- Un atlas pour enfants avec des illustrations captivantes \n"
                                        "- Un abonnement à un magazine éducatif pour enfants")))
    
    @Rule(Cadeau(age="6-9ans", sexe="masculin", interest="sport", occasion="récompense_scolaire"))
    def garcon_recompense_sport(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Des patins à roulettes ou un skateboard pour débutants \n"
                                        "- Des vêtements ou chaussures de sport personnalisés \n"
                                        "- Un sac de sport pratique pour transporter ses affaires \n"
                                        "- Une montre connectée adaptée pour enfants pour suivre son activité \n"
                                        "- Un abonnement à un cours de sport ou à une activité en club \n"
                                        "- Un kit de frisbee ou de jeu d’extérieur interactif \n"
                                        "- Une raquette de tennis ou de badminton avec un set de volants")))

    @Rule(Cadeau(age="6-9ans", sexe="masculin", interest="activités_artistiques", occasion="récompense_scolaire"))
    def garcon_recompense_art(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Un kit de création de figurines en argile ou pâte à modeler \n"
                                        "- Un coffret de construction de mini-décors ou dioramas \n"
                                        "- Une boîte de sable magique pour des créations artistiques en 3D \n"
                                        "- Un coffret de création de bijoux (perles, fils, breloques) \n"
                                        "- Un set de pâte à modeler ou de sculpture pour créer des formes artistiques \n"
                                        "- Un livre d'activités DIY (Do It Yourself) adapté à son âge \n")))
