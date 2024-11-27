from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

# subclass of InterfaceEngine
class InterfaceEngine_12_17ans(InterfaceEngine):
    #fille------------------------------------------------------------------------------------------------------------------
    #anniversaire
    @Rule(Cadeau(age="12-17ans", sexe="feminine", interest="jeux_vidéo", occasion="anniversaire"))
    def fille_anniversaire_jeux_video(self):
        self.declare(Resultat(result=("Pour une adolescente aimant les jeux vidéo, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Une console de jeux (Nintendo Switch, PS5, Xbox) \n"
                                        "- Des jeux vidéo populaires (Minecraft, Fortnite, Animal Crossing) \n"
                                        "- Un casque gaming \n"
                                        "- Des accessoires de gaming (manette, tapis de souris RGB) \n"
                                        "- Une carte cadeau pour acheter des jeux en ligne \n"
                                        "- Des figurines ou des objets dérivés de ses jeux favoris (posters, vêtements, bijoux, etc.) \n"
                                        "- Un abonnement à un service de jeux (Xbox Game Pass, Nintendo Switch Online)")))

    @Rule(Cadeau(age="12-17ans", sexe="feminine", interest="livres", occasion="anniversaire"))
    def fille_anniversaire_livre(self):
        self.declare(Resultat(result=("Pour une adolescente aimant les livres, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Une collection de contes classiques illustrés \n"
                                        "- Une série de livres d'aventures pour enfants (ex. \"La Cabane Magique\") \n"
                                        "- Un livre interactif avec activités ou autocollants \n"
                                        "- Un carnet d'histoires personnalisable où elle peut écrire ses propres histoires \n"
                                        "- Une bande dessinée ou un roman graphique adapté à son âge (ex. \"Les Sisters\", \"Mortelle Adèle\")")))

    @Rule(Cadeau(age="12-17ans", sexe="feminine", interest="sport", occasion="anniversaire"))
    def fille_anniversaire_sport(self):
        self.declare(Resultat(result=("Pour une adolescente aimant le sport, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un kit de gymnastique ou de danse (tapis, rubans, chaussons) \n"
                                        "- Une corde à sauter colorée ou un jeu de fitness pour enfants \n"
                                        "- Un vélo ou une trottinette avec accessoires (casque, panier) \n"
                                        "- Un ballon adapté à son sport préféré (ex. football, basket, volleyball) \n"
                                        "- Une raquette et des volants pour jouer au badminton")))

    @Rule(Cadeau(age="12-17ans", sexe="feminine", interest="kits_scientifiques", occasion="anniversaire"))
    def fille_anniversaire_kit_scientifique(self):
        self.declare(Resultat(result=("Pour une adolescente aimant les kits scientifiques, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un kit de chimie pour réaliser des expériences sécurisées \n"
                                        "- Un microscope avec accessoires \n"
                                        "- Un kit de robotique pour construire un robot programmable \n"
                                        "- Un kit d'astronomie avec un petit télescope \n"
                                        "- Un kit d'exploration géologique avec des fossiles et minéraux \n"
                                        "- Un livre interactif ou éducatif sur les sciences")))

    @Rule(Cadeau(age="12-17ans", sexe="feminine", interest="musique", occasion="anniversaire"))
    def fille_anniversaire_musique(self):
        self.declare(Resultat(result=("Pour une adolescente aimant la musique, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un casque audio ou des écouteurs de haute qualité \n"
                                        "- Un abonnement à un service de streaming musical (Spotify, Apple Music, Deezer, etc.) \n"
                                        "- Un instrument de musique pour débutants ou amateurs (guitare, ukulélé, clavier) \n"
                                        "- Un carnet de composition pour écrire ses propres chansons \n"
                                        "- Une enceinte Bluetooth portable pour écouter de la musique partout")))

    #fille-------------------------------------------------------------------------------------------------------------------
    #Succès académique
    @Rule(Cadeau(age="12-17ans", sexe="feminine", interest="jeux_vidéo", occasion="succès_académique"))
    def fille_succès_académique_jeux_video(self):
        self.declare(Resultat(result=("Pour une adolescente aimant la jeux vidéo, voici des idées de cadeaux pour son succès académique : \n"
                                        "- Un kit de développement pour apprendre à créer ses propres jeux vidéo \n"
                                        "- Un accessoire ergonomique comme un support pour console ou des grips pour manette \n"
                                        "- Un clavier ou une souris gamer personnalisée \n"
                                        "- Une lampe ou décoration LED sur le thème des jeux vidéo \n"
                                        "- Une figurine ou goodies liés à son jeu préféré \n"
                                        "- Une carte cadeau pour des plateformes comme Steam, PlayStation Store ou Nintendo eShop")))

    @Rule(Cadeau(age="12-17ans", sexe="feminine", interest="livres", occasion="succès_académique"))
    def fille_succès_académique_livre(self):
        self.declare(Resultat(result=("Pour une adolescente aimant les livres, voici des idées de cadeaux pour son succès académique : \n"
                                        "- Un livre de développement personnel pour enfants (ex. J'apprends à gérer mes émotions) \n"
                                        "- Un livre de recettes simples pour débuter en cuisine \n"
                                        "- Un coffret de livres sur la mythologie ou les légendes du monde \n"
                                        "- Une lampe de lecture design pour l'encourager à lire le soir \n"
                                        "- Un livre sur des héroïnes inspirantes et leurs histoires \n"
                                        "- Un coffret de livres sur la mythologie ou les légendes du monde \n"
                                        "- Un abonnement à un magazine éducatif pour enfants")))

    @Rule(Cadeau(age="12-17ans", sexe="feminine", interest="sport", occasion="succès_académique"))
    def fille_succès_académique_sport(self):
        self.declare(Resultat(result=("Pour une adolescente aimant le sport, voici des idées de cadeaux pour son succès académique : \n"
                                        "- Un tapis de yoga avec des motifs inspirants \n"
                                        "- Une mini table de ping-pong pliable pour jouer à la maison \n"
                                        "- Une tenue de sport personnalisée\n"
                                        "- Un sac de sport pratique pour transporter ses affaires \n"
                                        "- Un kit de tir à l’arc pour enfants pour s’initier en toute sécurité \n"
                                        "- Un kit de frisbee ou de jeu d’extérieur interactif \n"
                                        "- Une trottinette sportive avec des protections assorties")))

    @Rule(Cadeau(age="12-17ans", sexe="feminine", interest="kits_scientifiques", occasion="succès_académique"))
    def fille_succès_académique_kit_scientifique(self):
        self.declare(Resultat(result=("Pour une adolescente aimant les kits scientifiques, voici des idées de cadeaux pour son succès académique : \n"
                                        "- Un kit de chimie pour réaliser des expériences sécurisées \n"
                                        "- Un microscope adapté aux enfants avec accessoires \n"
                                        "- Un livre d'activités scientifiques avec des expériences faciles à réaliser \n"
                                        "- Un kit de jardinage scientifique pour cultiver des plantes et apprendre la botanique \n"
                                        "- Un télescope pour observer les étoiles et apprendre l'astronomie \n"
                                        "- Un kit d'expériences de chimie sécurisées \n"
                                        "- Un abonnement à un magazine scientifique pour enfants (comme Science & Vie Junior)")))

    @Rule(Cadeau(age="12-17ans", sexe="feminine", interest="musique", occasion="succès_académique"))
    def fille_succès_académique_musique(self):
        self.declare(Resultat(result=("Pour une adolescente aimant la musique, voici des idées de cadeaux pour son succès académique : \n"
                                        "- Un microphone pour enregistrer des chansons ou des podcasts \n"
                                        "- Un cours de musique ou un atelier (chant, guitare, piano, etc.) \n"
                                        "- Un album vinyle ou CD de son artiste préféré \n"
                                        "- Des accessoires musicaux, comme un porte-clés ou un t-shirt à l'effigie de ses artistes préférés \n"
                                        "- Une lampe ou décoration en forme d'instrument de musique")))


    #garcon------------------------------------------------------------------------------------------------------------------
    #anniversaire
    @Rule(Cadeau(age="12-17ans", sexe="masculin", interest="jeux_vidéo", occasion="anniversaire"))
    def garcon_anniversaire_jeux_video(self):
        self.declare(Resultat(result=("Pour un adolescent aimant les jeux vidéo, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un siège gaming confortable \n"
                                        "- Une souris gaming ou un clavier rétroéclairé \n"
                                        "- Une carte cadeau pour acheter des jeux ou des contenus en ligne (Steam, PlayStation Store, Xbox, etc.) \n"
                                        "- Une figurine ou un objet de collection inspiré de son jeu vidéo favori \n"
                                        "- Une lampe ou un décor LED à l'effigie de ses personnages préférés \n"
                                        "- Une manette ergonomique ou personnalisée pour sa console préférée")))

    @Rule(Cadeau(age="12-17ans", sexe="masculin", interest="livres", occasion="anniversaire"))
    def garcon_anniversaire_livre(self):
        self.declare(Resultat(result=("Pour un adolescent aimant les livres, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un livre de science-fiction ou de fantasy adapté à son âge \n"
                                        "- Une collection de livres d'aventures comme Le Club des Cinq ou Les aventures de Tintin \n"
                                        "- Un livre d'activités scientifiques ou de bricolage pour éveiller sa curiosité \n"
                                        "- Une encyclopédie illustrée sur les dinosaures, l'espace, ou les inventions \n"
                                        "- Une bande dessinée humoristique ou d'action comme Astérix, Lucky Luke, ou Spirou \n"
                                        "- Un guide illustré sur un sujet qui le passionne, comme les animaux ou les super-héros.")))

    @Rule(Cadeau(age="12-17ans", sexe="masculin", interest="sport", occasion="anniversaire"))
    def garcon_anniversaire_sport(self):
        self.declare(Resultat(result=("Pour un adolescent aimant le sport, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Une planche de skate de qualité ou des rollers avec un casque et des protections \n"
                                        "- Un kit de mini-buts ou un panier de basketball portable \n"
                                        "- Un vélo tout terrain ou un scooter pour les aventures en plein air \n"
                                        "- Un ensemble de matériel de pêche ou d'escalade pour une aventure en plein air \n"
                                        "- Un ballon adapté à son sport préféré (ex. football, basket, volleyball) \n"
                                        "- Des vêtements ou accessoires de sport personnalisés (maillot de son équipe favorite, gourde, sac de sport) \n"
                                        "- Un kit de boxe ou de self-défense pour débuter dans une discipline sportive \n")))

    @Rule(Cadeau(age="12-17ans", sexe="masculin", interest="kits_scientifiques", occasion="anniversaire"))
    def garcon_anniversaire_kit_scientifique(self):
        self.declare(Resultat(result=("Pour un adolescent aimant les kits scientifiques, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un set de fossiles à découvrir et analyser \n"
                                        "- Un kit d'astronomie pour observer les étoiles et en apprendre plus sur l'univers \n"
                                        "- Un microscope avec des échantillons pour explorer le monde invisible \n"
                                        "- Un kit de chimie avec des expériences amusantes à réaliser à la maison \n"
                                        "- Un kit d'énergie solaire pour fabriquer des appareils alimentés par le soleil.")))

    @Rule(Cadeau(age="12-17ans", sexe="masculin", interest="musique", occasion="anniversaire"))
    def garcon__anniversaire_musique(self):
        self.declare(Resultat(result=("Pour un adolescent aimant la musique, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Une application ou un logiciel pour apprendre ou créer de la musique \n"
                                        "- Un casque audio ou des écouteurs de haute qualité \n"
                                        "- Un abonnement à un service de streaming musical (Spotify, Apple Music, Deezer, etc.) \n"
                                        "- Un instrument de musique pour débutants ou amateurs (guitare, ukulélé, clavier) \n"
                                        "- Un carnet de composition pour écrire ses propres chansons \n"
                                        "- Une enceinte Bluetooth portable pour écouter de la musique partout")))

    #garcon------------------------------------------------------------------------------------------------------------------
    #Succès académique
    @Rule(Cadeau(age="12-17ans", sexe="masculin", interest="jeux_vidéo", occasion="succès_académique"))
    def garcon_succès_académique_jeux_video(self):
        self.declare(Resultat(result=("Pour un adolescent aimant les jeux vidéo, voici des idées de cadeaux pour son succès académique : \n"
                                        "- Un accessoire de jeu, comme une manette sans fil ou un casque de gaming \n"
                                        "- Un jeu vidéo de stratégie ou d'aventure adapté à son âge (ex. Minecraft, Fortnite) \n"
                                        "- Un set de figurines de collection de ses personnages de jeux favoris \n"
                                        "- Une carte cadeau pour sa plateforme de jeux préférée (Steam, PlayStation, Xbox) \n"
                                        "- Un fauteuil ergonomique ou un coussin de jeu pour améliorer son confort pendant les sessions de jeu \n"
                                        "- Un t-shirt ou une casquette avec le logo de son jeu ou de son personnage préféré.")))

    @Rule(Cadeau(age="12-17ans", sexe="masculin", interest="livres", occasion="succès_académique"))
    def garcon_succès_académique_livre(self):
        self.declare(Resultat(result=("Pour un adolescent aimant les livres, voici des idées de cadeaux pour son succès académique : \n"
                                        "- Un livre de science ludique pour enfants \n"
                                        "- Un livre sur les héros historiques ou des anecdotes fascinantes."
                                        "- Une lampe de lecture design pour l'encourager à lire le soir \n"
                                        "- Un livre sur les dinosaures ou les animaux, avec des images interactives \n"
                                        "- Un atlas pour enfants avec des illustrations captivantes \n"
                                        "- Un abonnement à un magazine éducatif pour enfants")))
    
    @Rule(Cadeau(age="12-17ans", sexe="masculin", interest="sport", occasion="succès_académique"))
    def garcon_succès_académique_sport(self):
        self.declare(Resultat(result=("Pour un adolescent aimant le sport, voici des idées de cadeaux pour son succès académique : \n"
                                        "- Des patins à roulettes ou un skateboard pour débutants \n"
                                        "- Des vêtements ou chaussures de sport personnalisés \n"
                                        "- Un sac de sport pratique pour transporter ses affaires \n"
                                        "- Une montre connectée adaptée pour enfants pour suivre son activité \n"
                                        "- Un abonnement à un cours de sport ou à une activité en club \n"
                                        "- Un kit de frisbee ou de jeu d’extérieur interactif \n"
                                        "- Une raquette de tennis ou de badminton avec un set de volants")))

    @Rule(Cadeau(age="12-17ans", sexe="masculin", interest="kits_scientifiques", occasion="succès_académique"))
    def garcon_succès_académique_kit_scientifique(self):
        self.declare(Resultat(result=("Pour un adolescent aimant les kits scientifiques, voici des idées de cadeaux pour son succès académique : \n"
                                        "- Un kit de robotique pour assembler et programmer des robots \n"
                                        "- Un microscope avec des échantillons pour découvrir le monde microscopique \n"
                                        "- Un puzzle 3D de système solaire ou de structures géométriques \n"
                                        "- Un télescope pour explorer le ciel et découvrir les planètes \n"
                                        "- Un kit d'expériences de chimie pour réaliser des réactions fascinantes à la maison \n"
                                        "- Un abonnement à un magazine scientifique pour enfants pour nourrir sa curiosité et ses découvertes.")))

    @Rule(Cadeau(age="12-17ans", sexe="masculin", interest="musique", occasion="succès_académique"))
    def fille_succès_académique_musique(self):
        self.declare(Resultat(result=("Pour une adolescente aimant la musique, voici des idées de cadeaux pour son succès académique : \n"
                                        "- Une place de concert ou un bon pour un festival musical \n"
                                        "- Un microphone pour enregistrer des chansons ou des podcasts \n"
                                        "- Un cours de musique ou un atelier (chant, guitare, piano, etc.) \n"
                                        "- Un album vinyle ou CD de son artiste préféré \n"
                                        "- Des accessoires musicaux, comme un porte-clés ou un t-shirt à l'effigie de ses artistes préférés \n"
                                        "- Une lampe ou décoration en forme d'instrument de musique")))