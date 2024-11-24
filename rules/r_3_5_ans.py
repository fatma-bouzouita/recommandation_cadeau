from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

# subclass of InterfaceEngine
class InterfaceEngine_3_5ans(InterfaceEngine):
    # masculin
    # Dessin
    @Rule(Cadeau(age="3-5ans", sexe="masculin", interest="dessin", occasion="anniversaire"))
    def garcon_dessin_anniversaire(self):
        self.declare(Resultat(result=(
        "Pour un garçon de 3 à 5 ans aimant le dessin, voici des idées de cadeaux pour stimuler sa créativité lors de son anniversaire : \n"
        "- Kit de dessin complet (feutres lavables, crayons, cahiers à colorier) \n"
        "- Tableau blanc/magnétique avec feutres et aimants éducatifs \n"
        "- Chevalet de peinture avec pinceaux et peinture non toxique \n"
    )))

    @Rule(Cadeau(age="3-5ans", sexe="masculin", interest="dessin", occasion="entrée_à_l'école"))
    def garcon_dessin_ecole(self):
        self.declare(Resultat(result=(
        "Ces cadeaux accompagneront parfaitement un enfant créatif qui entre à l'école et apprend à s'exprimer à travers le dessin:\n"
        "- Carnet d'écriture pour débutants\n"
        "- Trousse d'art portable pour l'école\n"
        "- Livres éducatifs pour apprendre à dessiner des formes simples\n"
    )))

    # Puzzles
    @Rule(Cadeau(age="3-5ans", sexe="masculin", interest="puzzles", occasion="anniversaire"))
    def garcon_puzzles_anniversaire(self):
        self.declare(Resultat(result=(
        "Les puzzles aident à développer la réflexion et la motricité fine, parfaits pour un cadeau d'anniversaire stimulant:\n"
        "- Puzzle éducatif sur les animaux\n"
        "- Puzzle en bois sur les chiffres et lettres\n"
        "- Puzzle 3D simple pour enfants (voiture, maison)\n"
    )))

    @Rule(Cadeau(age="3-5ans", sexe="masculin", interest="puzzles", occasion="entrée_à_l'école"))
    def garcon_puzzles_ecole(self):
        self.declare(Resultat(result=(
            "Les puzzles éducatifs sont parfaits pour associer apprentissage et amusement pour un garçon qui commence l'école :\n"
            "- Puzzle éducatif sur l'alphabet\n"
            "- Puzzle interactif avec des boutons sonores pour apprendre\n"
            "- Puzzle magnétique pour apprendre les couleurs et les formes\n"
        )))

    # Histoires
    @Rule(Cadeau(age="3-5ans", sexe="masculin", interest="histoires", occasion="anniversaire"))
    def garcon_histoires_anniversaire(self):
        self.declare(Resultat(result=(
            "Offrir des histoires captivantes pour un anniversaire encourage l'imagination et l'amour de la lecture dès le plus jeune âge :\n"
            "- Livre illustré sur les aventures d'animaux\n"
            "- Livre sonore ou interactif (sons d'animaux, instruments)\n"
            "- Coffret avec plusieurs contes classiques\n"
        )))

    @Rule(Cadeau(age="3-5ans", sexe="masculin", interest="histoires", occasion="entrée_à_l'école"))
    def garcon_histoires_ecole(self):
        self.declare(Resultat(result=(
            "Ces choix aident un jeune lecteur à entrer dans le monde de l'école avec confiance et curiosité :\n"
            "- Livre éducatif avec images pour apprendre à lire\n"
            "- Livre personnalisé où l'enfant est le héros\n"
            "- Histoires courtes avec autocollants pour accompagner la lecture\n"
        )))

    # Jeux éducatifs
    @Rule(Cadeau(age="3-5ans", sexe="masculin", interest="jeux_éducatifs", occasion="anniversaire"))
    def garcon_jeux_educatifs_anniversaire(self):
        self.declare(Resultat(result=(
            "Ces jeux éducatifs offrent une expérience amusante et enrichissante pour un garçon curieux célébrant son anniversaire :\n"
            "- Jeu de société éducatif pour apprendre les chiffres et les lettres\n"
            "- Kit de construction en blocs (Lego adaptés) pour stimuler la créativité\n"
            "- Jeu électronique interactif pour apprendre les formes et les sons\n"
            "- Jeu de mémoire avec cartes illustrées d'animaux ou de véhicules\n"
            "- Tablette éducative pour enfants avec activités préinstallées\n"
        )))

    @Rule(Cadeau(age="3-5ans", sexe="masculin", interest="jeux_éducatifs", occasion="entrée_à_l'école"))
    def garcon_jeux_educatifs_ecole(self):
        self.declare(Resultat(result=(
            "Ces jeux sont conçus pour soutenir l'apprentissage des concepts de base lors de l'entrée à l'école, tout en restant amusants :\n"
            "- Jeu de cartes éducatives pour apprendre les couleurs, formes et chiffres\n"
            "- Tableau interactif (alphabet, chiffres, images) pour un apprentissage ludique\n"
            "- Kit STEM pour enfants (science, technologie, ingénierie) pour éveiller la curiosité\n"
            "- Jeu de dominos colorés pour travailler la logique\n"
        )))

    # Divertissement
    @Rule(Cadeau(age="3-5ans", sexe="masculin", interest="divertissement", occasion="anniversaire"))
    def garcon_divertissement_anniversaire(self):
        self.declare(Resultat(result=(
            "Faites de son anniversaire un moment inoubliable avec des jeux divertissants qui éveillent son imagination et sa joie :\n"
            "- Voiture télécommandée robuste pour les jeunes conducteurs\n"
            "- Jeu interactif lumineux avec sons et musique (karaoké, piano lumineux)\n"
            "- Circuit de voiture ou de train simple pour débutants\n"
            "- Costume de super-héros ou d'aventurier pour des jeux de rôle\n"
            "- Kit de bulles de savon géantes pour jouer à l'extérieur\n"
        )))

    @Rule(Cadeau(age="3-5ans", sexe="masculin", interest="divertissement", occasion="entrée_à_l'école"))
    def garcon_divertissement_ecole(self):
        self.declare(Resultat(result=(
            "Ces cadeaux de divertissement apportent une touche de légèreté et de fun pour accompagner sa nouvelle routine scolaire :\n"
            "- Projecteur d'étoiles pour un coucher apaisant après l'école\n"
            "- Balle rebondissante ou ballon léger à motifs rigolos\n"
            "- Petit théâtre de marionnettes pour jouer des histoires\n"
            "- Toupies lumineuses avec effets sonores amusants\n"
            "- Jeu de quilles ou mini bowling adapté à l'intérieur\n"
        )))

    #fille
    # puzzle
    @Rule(Cadeau(age="3-5ans", sexe="feminine", interest="puzzles", occasion="anniversaire"))
    def fille_puzzles_anniversaire(self):
        self.declare(Resultat(result=(
            "Les puzzles aident à développer la réflexion et la motricité fine, parfaits pour un cadeau d'anniversaire stimulant :\n"
            "- Puzzle éducatif sur les princesses ou les animaux mignons\n"
            "- Puzzle en bois sur les chiffres et lettres colorés\n"
            "- Puzzle 3D simple pour enfants (château, maison de poupée)\n"
        )))

    @Rule(Cadeau(age="3-5ans", sexe="feminine", interest="puzzles", occasion="entrée_à_l'école"))
    def fille_puzzles_ecole(self):
        self.declare(Resultat(result=(
            "Ces puzzles éducatifs sont idéaux pour associer apprentissage et amusement pour une fille qui commence l'école :\n"
            "- Puzzle éducatif sur l'alphabet et les couleurs\n"
            "- Puzzle interactif avec des boutons sonores et images colorées\n"
            "- Puzzle magnétique pour apprendre les formes et les animaux\n"
        )))

        #histoires
    @Rule(Cadeau(age="3-5ans", sexe="feminine", interest="histoires", occasion="anniversaire"))
    def fille_histoires_anniversaire(self):
        self.declare(Resultat(result=(
        "Offrir des histoires captivantes pour un anniversaire encourage l'imagination et l'amour de la lecture dès le plus jeune âge :\n"
        "- Livre illustré sur les contes de princesses et aventures fantastiques\n"
        "- Livre sonore ou interactif (sons d'animaux ou de musique féerique)\n"
        "- Coffret contenant plusieurs contes classiques pour enfants\n"
    )))

    @Rule(Cadeau(age="3-5ans", sexe="feminine", interest="histoires", occasion="entrée_à_l'école"))
    def fille_histoires_ecole(self):
        self.declare(Resultat(result=(
        "Ces histoires aideront une jeune lectrice à aborder l'école avec curiosité et confiance :\n"
        "- Livre éducatif illustré pour apprendre à lire les premiers mots\n"
        "- Livre personnalisé avec l'enfant comme héroïne\n"
        "- Histoires interactives avec autocollants à ajouter sur les pages\n"
    )))
    #jeux_éducatifs
    @Rule(Cadeau(age="3-5ans", sexe="feminine", interest="jeux_éducatifs", occasion="anniversaire"))
    def fille_jeux_educatifs_anniversaire(self):
        self.declare(Resultat(result=(
        "Ces jeux éducatifs sont parfaits pour un anniversaire tout en s'amusant et en apprenant :\n"
        "- Jeu de société éducatif pour apprendre les couleurs et les chiffres\n"
        "- Kit de construction créatif (blocs en forme de fleurs ou animaux)\n"
        "- Jeu électronique interactif pour apprendre les lettres et sons\n"
        "- Jeu de mémoire illustré avec des personnages de contes\n"
        "- Tablette éducative pour enfants avec activités ludiques\n"
    )))

    @Rule(Cadeau(age="3-5ans", sexe="feminine", interest="jeux_éducatifs", occasion="entrée_à_l'école"))
    def fille_jeux_educatifs_ecole(self):
        self.declare(Resultat(result=(
        "Ces jeux soutiennent l'apprentissage des concepts de base de manière amusante pour une rentrée réussie :\n"
        "- Jeu de cartes éducatives pour apprendre les formes et les couleurs\n"
        "- Tableau interactif avec alphabet, chiffres et illustrations amusantes\n"
        "- Kit STEM adapté aux jeunes filles pour éveiller la curiosité scientifique\n"
        "- Jeu de dominos colorés pour travailler la logique et l'observation\n"
    )))
    # divertissement
    @Rule(Cadeau(age="3-5ans", sexe="feminine", interest="divertissement", occasion="anniversaire"))
    def fille_divertissement_anniversaire(self):
        self.declare(Resultat(result=(
        "Faites de son anniversaire un moment magique avec des cadeaux divertissants :\n"
        "- Maison de poupées miniature avec accessoires\n"
        "- Jeu interactif lumineux et musical (karaoké, danse)\n"
        "- Costume de princesse ou de fée pour des jeux de rôle créatifs\n"
        "- Kit pour fabriquer des bulles géantes pour jouer à l'extérieur\n"
        "- Ensemble de perles pour créer ses propres bijoux\n"
    )))

    @Rule(Cadeau(age="3-5ans", sexe="feminine", interest="divertissement", occasion="entrée_à_l'école"))
    def fille_divertissement_ecole(self):
        self.declare(Resultat(result=(
        "Ces idées de divertissement apportent un moment de joie et de détente après une journée à l'école :\n"
        "- Projecteur d'étoiles ou de motifs féeriques pour apaiser le coucher\n"
        "- Jouet rebondissant ou ballon à motifs fantaisie\n"
        "- Petit théâtre de marionnettes pour raconter des histoires\n"
        "- Toupies lumineuses pour jouer à l'intérieur\n"
        "- Jeu de quilles ou mini bowling aux couleurs pastel\n"
    )))
    # dessin
    @Rule(Cadeau(age="3-5ans", sexe="feminine", interest="dessin", occasion="anniversaire"))
    def fille_dessin_anniversaire(self):
        self.declare(Resultat(result=(
        "Encouragez sa créativité avec ces cadeaux parfaits pour une petite artiste :\n"
        "- Kit de dessin complet avec feutres lavables, crayons et papiers à colorier\n"
        "- Chevalet avec tableau double face (craie et feutre) pour varier les styles\n"
        "- Ensemble de tampons encreurs avec motifs d'animaux ou de princesses\n"
        "- Livres de coloriage sur le thème des contes ou des animaux mignons\n"
        "- Pâte à modeler colorée avec outils pour dessiner en relief\n"
    )))
    @Rule(Cadeau(age="3-5ans", sexe="feminine", interest="dessin", occasion="entrée_à_l'école"))
    def fille_dessin_ecole(self):
        self.declare(Resultat(result=(
        "Ces idées ludiques pour le dessin sont idéales pour compléter sa rentrée scolaire :\n"
        "- Trousse d'art portable pour emporter partout ses crayons et feutres\n"
        "- Carnet de dessin avec pages pré-imprimées pour s'entraîner à dessiner des formes\n"
        "- Tableau magnétique éducatif avec lettres et chiffres à tracer\n"
        "- Peinture à l'eau non toxique avec pinceaux adaptés à son âge\n"
        "- Livres éducatifs sur les bases du dessin, comme apprendre les formes et les couleurs\n"
    )))








