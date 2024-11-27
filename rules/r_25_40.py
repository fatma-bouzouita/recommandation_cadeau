from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

# subclass of InterfaceEngine
class InterfaceEngine_25_40ans(InterfaceEngine):
    # femme
    # anniversaire
    @Rule(Cadeau(age="25-40ans", sexe="feminine", interest="mode", occasion="anniversaire"))
    def femme_anniversaire_mode(self):
        self.declare(Resultat(result=("Pour une femme passionnée de mode, voici des idées de cadeaux pour son anniversaire : \n"
                                  "- Une carte cadeau dans une boutique de vêtements\n"
                                  "- Des bijoux tendance\n"
                                  "- Un abonnement à un magazine de mode"
                                  "- Des bijoux tendance\n"
                                  "- Un cours de stylisme ou un atelier de création\n"
                                  "- Une paire de chaussures élégantes\n"
                                  "- Un sac à main de marque\n"
                                  "- Un parfum de luxe\n"
                                  "- Un foulard ou une écharpe en soie")))
        
    @Rule(Cadeau(age="25-40ans", sexe="feminine", interest="voyage", occasion="anniversaire"))
    def femme_anniversaire_voyage(self):
        self.declare(Resultat(result=("Pour une femme passionnée de voyage, voici des idées de cadeaux pour son anniversaire: \n"
                                  "- Une valise de qualité ou un sac à dos élégant\n"
                                  "- Une carte du monde interactive\n"
                                  "- Un coffret d'expérience ou un guide de voyage\n"
                                  "- Un abonnement à un service de location de logements (Airbnb, etc.)\n"
                                  "- Un coussin ou une couverture de voyage confortable\n"
                                  "- Un appareil photo instantané ou portable\n"
                                  "- Des accessoires de voyage pratiques (trousse de toilette, adaptateur universel)")))

    @Rule(Cadeau(age="25-40ans", sexe="feminine", interest="technologie", occasion="anniversaire"))
    def femme_anniversaire_technologie(self):
        self.declare(Resultat(result=("Pour une femme intéressée par la technologie, voici des idées de cadeaux pour son anniversaire: \n"
                                  "- Un gadget high-tech (écouteurs sans fil, smartwatch)\n"
                                  "- Une liseuse électronique\n"
                                  "- Un abonnement à une plateforme de streaming ou de-learning\n"
                                  "- Une caméra de vlog ou un anneau lumineux\n"
                                  "- Une tablette graphique pour créativité numérique\n"
                                  "- Une imprimante photo portable\n"
                                  "- Un chargeur sans fil élégant\n"
                                  "- Une station de recharge multi-appareils")))

    @Rule(Cadeau(age="25-40ans", sexe="feminine", interest="sport", occasion="anniversaire"))
    def femme_anniversaire_sport(self):
        self.declare(Resultat(result=("Pour une femme sportive, voici des idées de cadeaux pour son anniversaire : \n"
                                  "- Une tenue de sport élégante\n"
                                  "- Un tapis de yoga ou des haltères\n"
                                  "- Une montre connectée pour suivre ses performances\n"
                                  "- Une paire de baskets adaptées à son activité\n"
                                  "- Une gourde isotherme haut de gamme\n"
                                  "- Une corde à sauter intelligente\n"
                                  "- Un sac de sport fonctionnel et stylé")))

    @Rule(Cadeau(age="25-40ans", sexe="feminine", interest="cuisine", occasion="anniversaire"))
    def femme_anniversaire_cuisine(self):
        self.declare(Resultat(result=("Pour une femme passionnée de cuisine, voici des idées de cadeaux pour son anniversaire : \n"
                                  "- Un robot multifonction ou un gadget de cuisine\n"
                                  "- Un livre de recettes ou un abonnement à une box culinaire\n"
                                  "- Un cours de cuisine en groupe ou en ligne\n"
                                  "- Une cocotte en fonte de qualité\n"
                                  "- Une planche à découper gravée\n"
                                  "- Une box dingrédients premium (huiles, épices)\n"
                                  "- Une machine à pâtes ou un appareil à raclette/fondue")))
        
    @Rule(Cadeau(age="25-40ans", sexe="feminine", interest="décoration", occasion="anniversaire"))
    def femme_anniversaire_decoration(self):
        self.declare(Resultat(result=("Pour une femme passionnée de décoration, voici des idées de cadeaux pour son anniversaire : \n"
                                  "- Une lampe design ou un objet de décoration moderne\n"
                                  "- Un coffret de bougies parfumées haut de gamme\n"
                                  "- Des cadres photo personnalisés\n"
                                  "- Une plante d'intérieur ou un pot en céramique original\n"
                                  "- Un tableau ou une illustration décorative\n"
                                  "- Des coussins ou plaids élégants pour le salon\n"
                                  "- Un miroir décoratif unique")))
        
    @Rule(Cadeau(age="25-40ans", sexe="feminine", interest="art", occasion="anniversaire"))
    def femme_anniversaire_art(self):
        self.declare(Resultat(result=("Pour une femme passionnée d'art, voici des idées de cadeaux pour son anniversaire : \n"
                                  "- Une reproduction d'une œuvre d'art célèbre\n"
                                  "- Un kit de peinture ou de dessin\n"
                                  "- Un abonnement à des expositions d'art ou un pass musée\n"
                                  "- Un livre sur lhistoire de lart ou un artiste spécifique\n"
                                  "- Une sculpture ou une pièce d'art moderne pour sa maison\n"
                                  "- Un stage ou atelier d’art (peinture, poterie, etc.)\n"
                                  "- Une impression personnalisée d’un tableau qu’elle adore\n"
                                  "- Des fournitures haut de gamme pour la création artistique")))
        
    @Rule(Cadeau(age="25-40ans", sexe="feminine", interest="livres", occasion="anniversaire"))
    def femme_anniversaire_livres(self):
        self.declare(Resultat(result=("Pour une femme passionnée de livres, voici des idées de cadeaux pour son anniversaire : \n"
                                  "- Une liseuse électronique comme Kindle\n"
                                  "- Une édition collector de son auteur préféré\n"
                                  "- Un abonnement à un club de lecture ou à une box littéraire\n"
                                  "- Des marque-pages personnalisés ou faits main\n"
                                  "- Un livre de développement personnel ou un roman tendance\n"
                                  "- Un carnet pour prendre des notes de lecture\n"
                                  "- Une lampe de lecture portable et élégante\n"
                                  "- Une bibliothèque murale compacte et design")))

    # mariage

    @Rule(Cadeau(age="25-40ans", sexe="feminine", interest="mode", occasion="mariage"))
    def femme_mariage_mode(self):
        self.declare(Resultat(result=("Pour une femme passionnée de mode, voici des idées de cadeaux pour un mariage : \n"
                                    "- Une pochette élégante ou un foulard de luxe\n"
                                    "- Un coffret de bijoux de créateur\n"
                                    "- Un abonnement à une box de mode\n"
                                    "- Une carte cadeau pour un service de personnalisation\n"
                                    "- Une séance photo de mode professionnelle\n"
                                    "- Une robe ou un vêtement personnalisé pour l’occasion\n"
                                    "- Une paire de lunettes de soleil chic\n"
                                    "- Un coffret de parfums ou d’accessoires de mode")))
        
    @Rule(Cadeau(age="25-40ans", sexe="feminine", interest="voyage", occasion="mariage"))
    def femme_mariage_voyage(self):
        self.declare(Resultat(result=("Pour une femme passionnée de voyage, voici des idées de cadeaux pour un mariage : \n"
                                    "- Une carte du monde à gratter\n"
                                    "- Un coffret voyage (séjour ou expérience unique)\n"
                                    "- Un kit d accessoires pour ses déplacements (étiquette, trousse de voyage)\n"
                                    "- Un sac de voyage haut de gamme\n"
                                    "- Un guide de voyage personnalisé pour sa lune de miel\n"
                                    "- Une trousse de maquillage ou d’hygiène de voyage\n"
                                    "- Un ensemble de bagages assortis\n"
                                    "- Un hamac de voyage portable pour ses aventures")))

    @Rule(Cadeau(age="25-40ans", sexe="feminine", interest="technologie", occasion="mariage"))
    def femme_mariage_technologie(self):
        self.declare(Resultat(result=("Pour une femme amoureuse de la technologie, voici des idées de cadeaux pour un mariage : \n"
                                    "- Un appareil photo instantané\n"
                                    "- Un casque audio ou des écouteurs haut de gamme\n"
                                    "- Une lampe connectée design pour la maison\n"
                                    "- Une enceinte Bluetooth élégante\n"
                                    "- Un assistant vocal intelligent (comme Alexa ou Google Home)\n"
                                    "- Une station de charge sans fil pour plusieurs appareils\n"
                                    "- Un cadre photo numérique connecté\n"
                                    "- Un projecteur portable pour soirées cinéma à domicile")))

    @Rule(Cadeau(age="25-40ans", sexe="feminine", interest="sport", occasion="mariage"))
    def femme_mariage_sport(self):
        self.declare(Resultat(result=("Pour une femme sportive, voici des idées de cadeaux pour un mariage : \n"
                                    "- Un abonnement à une salle de sport ou un programme en ligne\n"
                                    "- Un vélo dintérieur ou un accessoire de fitness\n"
                                    "- Une tenue sportive haut de gamme\n"
                                    "- Un tracker de fitness avancé\n"
                                    "- Un tapis de yoga de luxe\n"
                                    "- Une bouteille d’eau réutilisable personnalisée\n"
                                    "- Une séance de coaching sportif privé\n"
                                    "- Un équipement pour sports en extérieur, comme des bâtons de randonnée ou des accessoires de trekking")))

    @Rule(Cadeau(age="25-40ans", sexe="feminine", interest="cuisine", occasion="mariage"))
    def femme_mariage_cuisine(self):
        self.declare(Resultat(result=("Pour une femme passionnée de cuisine, voici des idées de cadeaux pour un mariage : \n"
                                      "- Un set dustensiles de cuisine haut de gamme\n"
                                      "- Une machine à café ou un blender puissant\n"
                                      "- Un cours de pâtisserie ou de cuisine gastronomique\n"
                                      "- Une collection d épices rares ou premium\n"
                                      "- Un livre de cuisine avec des recettes internationales\n"
                                      "- Un barbecue portable ou un grill d’intérieur\n"
                                      "- Une balance électronique design\n"
                                      "- Un ensemble de couteaux de chef professionnels"))) 
               
    @Rule(Cadeau(age="25-40ans", sexe="feminine", interest="décoration", occasion="mariage"))
    def femme_mariage_decoration(self):
        self.declare(Resultat(result=("Pour une femme passionnée de décoration, voici des idées de cadeaux pour un mariage : \n"
                                  "- Un vase en verre soufflé ou une pièce artisanale unique\n"
                                  "- Un tableau décoratif ou une peinture murale élégante\n"
                                  "- Un set de linge de maison de qualité (nappe, serviettes, etc.)\n"
                                  "- Des bougies décoratives ou des diffuseurs d’arôme\n"
                                  "- Une décoration murale personnalisée ou gravée pour célébrer l’événement\n"
                                  "- Une horloge murale design\n"
                                  "- Une lampe à poser ou suspension unique\n"
                                  "- Un tapis élégant ou coussin tendance pour le salon")))
        
    @Rule(Cadeau(age="25-40ans", sexe="feminine", interest="art", occasion="mariage"))
    def femme_mariage_art(self):
        self.declare(Resultat(result=("Pour une femme passionnée d'art, voici des idées de cadeaux pour un mariage : \n"
                                  "- Une sculpture ou un objet dart contemporain\n"
                                  "- Un tableau ou une illustration personnalisée pour le couple\n"
                                  "- Un abonnement à une galerie dart ou des billets pour des expositions\n"
                                  "- Un kit de création artistique (peinture, sculpture, etc.)\n"
                                  "- Une œuvre d’un artiste local ou une pièce unique de collection\n"
                                  "- Un carnet de croquis de qualité\n"
                                  "- Un stage ou atelier artistique pour débutants\n"
                                  "- Une peinture murale ou fresque personnalisée pour leur maison")))
        
    @Rule(Cadeau(age="25-40ans", sexe="feminine", interest="livres", occasion="mariage"))
    def femme_mariage_livres(self):
        self.declare(Resultat(result=("Pour une femme passionnée de livres, voici des idées de cadeaux pour un mariage : \n"
                                  "- Une collection dœuvres littéraires classiques ou romantiques\n"
                                  "- Un livre de recettes élégamment illustré\n"
                                  "- Une édition spéciale sur lart du mariage ou des traditions culturelles\n"
                                  "- Un carnet de notes en cuir ou un journal personnalisé\n"
                                  "- Un abonnement à un service de livraison de livres ou à une bibliothèque numérique\n"
                                  "- Un livre interactif ou avec des illustrations immersives\n"
                                  "- Une liseuse électronique avec sa bibliothèque initiale\n"
                                  "- Un livre inspirant sur les voyages ou le développement personnel")))




