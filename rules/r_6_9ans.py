from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

# subclass of InterfaceEngine
class InterfaceEngine_6_9ans(InterfaceEngine):
    #fille
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
    def fille_anniversaire_construction(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Une collection de contes classiques illustrés \n"
                                        "- Une série de livres d'aventures pour enfants (ex. \"La Cabane Magique\") \n"
                                        "- Un livre interactif avec activités ou autocollants \n"
                                        "- Un carnet d'histoires personnalisable où elle peut écrire ses propres histoires \n"
                                        "- Une bande dessinée ou un roman graphique adapté à son âge (ex. \"Les Sisters\", \"Mortelle Adèle\")")))

    @Rule(Cadeau(age="6-9ans", sexe="feminine", interest="sport", occasion="anniversaire"))
    def fille_anniversaire_construction(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Un kit de gymnastique ou de danse (tapis, rubans, chaussons) \n"
                                        "- Une corde à sauter colorée ou un jeu de fitness pour enfants \n"
                                        "- Un vélo ou une trottinette avec accessoires (casque, panier) \n"
                                        "- Un ballon adapté à son sport préféré (ex. football, basket, volleyball) \n"
                                        "- Une raquette et des volants pour jouer au badminton")))

    @Rule(Cadeau(age="6-9ans", sexe="feminine", interest="activités_artistiques", occasion="anniversaire"))
    def fille_anniversaire_construction(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Un kit de peinture avec chevalet, pinceaux et aquarelles \n"
                                        "- Un coffret de création de bijoux (perles, fils, breloques) \n"
                                        "- Un livre ou un kit de coloriage géant avec des feutres et crayons \n"
                                        "- Un set de pâte à modeler ou de sculpture pour créer des formes artistiques \n"
                                        "- Un kit de broderie ou de couture simple pour débutants")))
    
    #fille
    #Récompense scolaire
    @Rule(Cadeau(age="6-9ans", sexe="feminine", interest="jeux_de_construction", occasion="récompense_scolaire"))
    def fille_anniversaire_construction(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Un coffret Lego Friends ou Lego Disney \n"
                                        "- Un kit Meccano pour créer des modèles amusants \n"
                                        "- Puzzles 3D\n"
                                        "- Kit de bricolage pour construire des bijoux ou accessoires\n"
                                        "- Un jeu de construction STEM pour apprendre en s'amusant \n"
                                        "- Un ensemble de blocs de construction en bois colorés")))
        
    @Rule(Cadeau(age="6-9ans", sexe="feminine", interest="livres", occasion="récompense_scolaire"))
    def fille_anniversaire_construction(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Un livre de science ludique pour enfants \n"
                                        "- Une bande dessinée adaptée à son âge (ex. Mortelle Adèle, Les Sisters) \n"
                                        "- Une lampe de lecture design pour l'encourager à lire le soir \n"
                                        "- Un livre sur des héroïnes inspirantes et leurs histoires \n"
                                        "- Un carnet personnalisé pour écrire ses propres histoires \n"
                                        "- Un abonnement à un magazine éducatif pour enfants")))
    
    @Rule(Cadeau(age="6-9ans", sexe="feminine", interest="sport", occasion="récompense_scolaire"))
    def fille_anniversaire_construction(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        
                                        "- Une raquette et des volants pour jouer au badminton")))

    @Rule(Cadeau(age="6-9ans"), Cadeau(interest="sport"))
    def cadeau_enfant_sport(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                        "- Ballon de football \n"
                                        "- Trottinette \n"
                                        "- Mini-table de ping-pong")))