from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

# subclass of InterfaceEngine
class InterfaceEngine_25_40ans(InterfaceEngine):
    #femme------------------------------------------------------------------------------------------------------------------
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


    #homme------------------------------------------------------------------------------------------------------------------
    # anniversaire
    @Rule(Cadeau(age="25-40ans", sexe="masculin", interest="mode", occasion="anniversaire"))
    def homme_anniversaire_mode(self):
        self.declare(Resultat(result=("Pour un homme passionné de mode, voici des idées de cadeaux pour son anniversaire : \n"
                                    "- Une montre de luxe ou une montre vintage\n"
                                    "- Un portefeuille en cuir de créateur\n"
                                    "- Un costume sur mesure ou un blazer élégant\n"
                                    "- Un sac à dos ou une valise design\n"
                                    "- Un abonnement à un service de mode en ligne\n"
                                    "- Des lunettes de soleil haut de gamme\n"
                                    "- Une ceinture en cuir de designer\n"
                                    "- Un parfum signature\n"
                                    "- Un porte-clés personnalisé\n")))

    @Rule(Cadeau(age="25-40ans", sexe="masculin", interest="décoration", occasion="anniversaire"))
    def homme_anniversaire_decoration(self):
        self.declare(Resultat(result=("Pour un homme passionné de décoration, voici des idées de cadeaux pour son anniversaire : \n"
                                    "- Un tableau moderne ou une affiche encadrée de style contemporain\n"
                                    "- Une sculpture minimaliste ou un objet déco en métal\n"
                                    "- Un meuble design ou une étagère originale\n"
                                    "- Une lampe d’ambiance élégante\n"
                                    "- Un vase en verre ou en céramique artisanale\n"
                                    "- Un set de décoration murale avec des photographies en édition limitée\n"
                                    "- Une horloge murale vintage\n"
                                    "- Une chaise design ou un fauteuil unique\n"
                                    "- Un tapis moderne et élégant")))

    @Rule(Cadeau(age="25-40ans", sexe="masculin", interest="voyage", occasion="anniversaire"))
    def homme_anniversaire_voyage(self):
        self.declare(Resultat(result=("Pour un homme passionné de voyage, voici des idées de cadeaux pour son anniversaire : \n"
                                    "- Un sac à dos de voyage durable ou une valise de qualité\n"
                                    "- Une montre de voyage avec multiple fuseaux horaires\n"
                                    "- Un kit de voyage avec des accessoires pratiques (adaptateur, oreiller, etc.)\n"
                                    "- Un guide touristique ou un abonnement à un service de voyage\n"
                                    "- Une expérience de voyage comme une excursion en montgolfière ou une plongée sous-marine\n"
                                    "- Un carnet de voyage en cuir ou un journal personnalisé\n"
                                    "- Une boussole moderne ou un accessoire de randonnée\n"
                                    "- Une carte du monde à gratter\n"
                                    "- Un guide gastronomique pour découvrir de nouvelles destinations")))

    @Rule(Cadeau(age="25-40ans", sexe="masculin", interest="livres", occasion="anniversaire"))
    def homme_anniversaire_livres(self):
        self.declare(Resultat(result=("Pour un homme passionné de livres, voici des idées de cadeaux pour son anniversaire : \n"
                                    "- Une édition collector d’un auteur classique\n"
                                    "- Un abonnement à un service de livres audio ou un club de lecture\n"
                                    "- Un livre de développement personnel ou un guide de productivité\n"
                                    "- Un roman graphique ou une BD de science-fiction\n"
                                    "- Un livre sur la cuisine ou un ouvrage sur l’art de vivre\n"
                                    "- Un recueil de poèmes ou de littérature contemporaine\n"
                                    "- Un livre sur l’histoire de la musique ou du cinéma\n"
                                    "- Un roman d’aventure ou de voyage\n"
                                    "- Un livre d'art ou une biographie d’artiste")))

    @Rule(Cadeau(age="25-40ans", sexe="masculin", interest="technologie", occasion="anniversaire"))
    def homme_anniversaire_technologie(self):
        self.declare(Resultat(result=("Pour un homme passionné de technologie, voici des idées de cadeaux pour son anniversaire : \n"
                                    "- Un casque audio de haute qualité\n"
                                    "- Une caméra d’action (GoPro ou autre)\n"
                                    "- Un gadget pour la maison connectée (éclairage intelligent, thermostat, etc.)\n"
                                    "- Un chargeur sans fil ou une station de recharge élégante\n"
                                    "- Un drone ou un accessoire de réalité virtuelle\n"
                                    "- Une montre connectée ou un bracelet de suivi d’activité\n"
                                    "- Un appareil photo instantané\n"
                                    "- Une enceinte Bluetooth haut de gamme\n"
                                    "- Une batterie portable de grande capacité")))

    @Rule(Cadeau(age="25-40ans", sexe="masculin", interest="sport", occasion="anniversaire"))
    def homme_anniversaire_sport(self):
        self.declare(Resultat(result=("Pour un homme sportif, voici des idées de cadeaux pour son anniversaire : \n"
                                    "- Un abonnement à une salle de sport ou un programme d’entraînement en ligne\n"
                                    "- Un vélo de course ou un équipement sportif spécialisé\n"
                                    "- Un tracker de fitness ou une montre GPS dédiée au sport\n"
                                    "- Un sac de sport de qualité ou un kit d’entraînement personnel\n"
                                    "- Une paire de sneakers de sport haut de gamme\n"
                                    "- Un accessoire de fitness comme des haltères, des kettlebells ou un tapis de yoga\n"
                                    "- Un équipement pour la pratique du crossfit\n"
                                    "- Un vélo elliptique ou un rameur\n"
                                    "- Un abonnement à une plateforme de sport en ligne")))

    @Rule(Cadeau(age="25-40ans", sexe="masculin", interest="cuisine", occasion="anniversaire"))
    def homme_anniversaire_cuisine(self):
        self.declare(Resultat(result=("Pour un homme passionné de cuisine, voici des idées de cadeaux pour son anniversaire : \n"
                                    "- Un ensemble de couteaux de chef professionnels\n"
                                    "- Un barbecue haut de gamme ou une plancha\n"
                                    "- Un kit de préparation de cocktails ou un bar à domicile\n"
                                    "- Un livre de cuisine pour les gourmets ou un guide gastronomique\n"
                                    "- Une machine à café de qualité supérieure\n"
                                    "- Un cours de cuisine avec un chef ou une expérience culinaire unique\n"
                                    "- Un robot culinaire multifonction\n"
                                    "- Une planche à découper en bois massif personnalisée\n"
                                    "- Une machine à pâtes artisanale")))

    @Rule(Cadeau(age="25-40ans", sexe="masculin", interest="art", occasion="anniversaire"))
    def homme_anniversaire_art(self):
        self.declare(Resultat(result=("Pour un homme passionné d’art, voici des idées de cadeaux pour son anniversaire : \n"
                                    "- Une peinture contemporaine ou un tableau abstrait\n"
                                    "- Une sculpture moderne en métal ou en bois\n"
                                    "- Un abonnement à une galerie d’art ou à un musée\n"
                                    "- Un kit pour débuter en peinture ou en sculpture\n"
                                    "- Un livre d’art ou une biographie d’artiste\n"
                                    "- Une œuvre d’un artiste local ou une pièce unique de collection\n"
                                    "- Un art mural personnalisé\n"
                                    "- Un atelier d'art pour apprendre une nouvelle technique\n"
                                    "- Une pièce d'art vintage ou un objet déco inspiré d'un artiste")))

    # marriage
    @Rule(Cadeau(age="25-40ans", sexe="masculin", interest="mode", occasion="mariage"))
    def homme_mariage_mode(self):
        self.declare(Resultat(result=("Pour un homme passionné de mode à l’occasion d’un mariage, voici des idées de cadeaux : \n"
                                    "- Un costume ou un gilet personnalisé pour des occasions spéciales\n"
                                    "- Une montre de luxe gravée avec la date du mariage\n"
                                    "- Des boutons de manchette gravés ou en forme symbolique (cœurs, alliances)\n"
                                    "- Une pochette de costume brodée ou une cravate en soie raffinée\n"
                                    "- Une paire de chaussures en cuir élégantes, adaptées à des cérémonies\n"
                                    "- Un portefeuille en cuir gravé avec les initiales du couple\n"
                                    "- Un abonnement à un service de stylisme personnel pour ses tenues de cérémonie\n"
                                    "- Une écharpe ou une étole personnalisée pour les soirées spéciales")))

    @Rule(Cadeau(age="25-40ans", sexe="masculin", interest="décoration", occasion="mariage"))
    def homme_mariage_decoration(self):
        self.declare(Resultat(result=("Pour un homme passionné de décoration et pour célébrer le mariage, voici des idées de cadeaux : \n"
                                    "- Un tableau personnalisé représentant une scène romantique ou symbolique\n"
                                    "- Une horloge murale gravée avec la date du mariage\n"
                                    "- Une sculpture en métal ou en bois représentant l’union du couple\n"
                                    "- Des cadres photo personnalisés pour immortaliser les souvenirs de mariage\n"
                                    "- Une pièce décorative artisanale (vase ou lampe avec un design romantique)\n"
                                    "- Un set de bougies parfumées ou un diffuseur aux arômes apaisants pour le foyer conjugal\n"
                                    "- Une boîte de rangement gravée pour garder les souvenirs du mariage (cartes, photos, etc.)\n"
                                    "- Un service de vaisselle ou de décoration gravée avec les initiales du couple")))

    @Rule(Cadeau(age="25-40ans", sexe="masculin", interest="voyage", occasion="mariage"))
    def homme_mariage_voyage(self):
        self.declare(Resultat(result=("Pour un homme passionné de voyage à l’occasion de son mariage, voici des idées de cadeaux : \n"
                                    "- Une valise premium avec les initiales du couple\n"
                                    "- Un carnet de voyage personnalisé pour documenter leur lune de miel\n"
                                    "- Un drone compact pour capturer des souvenirs de leur voyage de noces\n"
                                    "- Une expérience de voyage exclusive (croisière, nuit dans un château, etc.)\n"
                                    "- Une carte du monde murale où ils peuvent marquer leurs destinations ensemble\n"
                                    "- Un kit de voyage de luxe (étiquettes gravées, accessoires pratiques)\n"
                                    "- Une pochette pour passeports ou documents avec leurs initiales\n"
                                    "- Un guide de voyage personnalisé pour leur destination de lune de miel")))

    @Rule(Cadeau(age="25-40ans", sexe="masculin", interest="livres", occasion="mariage"))
    def homme_mariage_livres(self):
        self.declare(Resultat(result=("Pour un homme passionné de livres et pour un mariage, voici des idées de cadeaux : \n"
                                    "- Une édition spéciale ou limitée sur l’amour ou les traditions nuptiales\n"
                                    "- Un album photo de mariage en cuir de style livre relié\n"
                                    "- Une biographie inspirante d’un couple ou d’un auteur sur l’amour\n"
                                    "- Un livre sur les voyages ou la gastronomie, dédié aux jeunes mariés\n"
                                    "- Un carnet de citations ou de poèmes personnalisés pour leur histoire\n"
                                    "- Un coffret de livres sur les cultures et cérémonies de mariage dans le monde\n"
                                    "- Un roman graphique romantique ou une bande dessinée spéciale\n"
                                    "- Un livre collaboratif où ils peuvent écrire ensemble leurs souvenirs à deux")))

    @Rule(Cadeau(age="25-40ans", sexe="masculin", interest="technologie", occasion="mariage"))
    def homme_mariage_technologie(self):
        self.declare(Resultat(result=("Pour un homme passionné de technologie à l’occasion d’un mariage, voici des idées de cadeaux : \n"
                                    "- Un appareil photo instantané pour capturer des moments spontanés\n"
                                    "- Une montre connectée avec un cadran gravé ou personnalisé\n"
                                    "- Une enceinte Bluetooth pour partager leur musique préférée ensemble\n"
                                    "- Un projecteur compact pour des soirées cinéma à la maison\n"
                                    "- Un assistant vocal personnalisé avec des routines spéciales pour le couple\n"
                                    "- Une lampe connectée romantique pour leurs moments à deux\n"
                                    "- Un cadre photo numérique pour afficher les souvenirs du mariage\n"
                                    "- Un robot domestique intelligent pour alléger leur quotidien à deux")))

    @Rule(Cadeau(age="25-40ans", sexe="masculin", interest="sport", occasion="mariage"))
    def homme_mariage_sport(self):
        self.declare(Resultat(result=("Pour un homme sportif à l’occasion d’un mariage, voici des idées de cadeaux : \n"
                                    "- Un abonnement à une activité sportive à faire en couple (yoga, danse, escalade)\n"
                                    "- Un vélo tandem pour des balades romantiques\n"
                                    "- Un tracker de fitness pour suivre leurs objectifs communs\n"
                                    "- Un équipement sportif personnalisé avec les initiales ou la date du mariage\n"
                                    "- Une tenue sportive assortie pour les deux\n"
                                    "- Un cours privé avec un coach dans son sport favori\n"
                                    "- Des accessoires pour des activités en plein air (tente, sac de randonnée pour deux)\n"
                                    "- Une expérience sportive à partager (rafting, kayak, randonnée guidée)")))

    @Rule(Cadeau(age="25-40ans", sexe="masculin", interest="cuisine", occasion="mariage"))
    def homme_mariage_cuisine(self):
        self.declare(Resultat(result=("Pour un homme passionné de cuisine à l’occasion d’un mariage, voici des idées de cadeaux : \n"
                                    "- Un set de couteaux gravés pour des préparations spéciales\n"
                                    "- Un barbecue haut de gamme pour partager des moments à deux\n"
                                    "- Un cours de cuisine gastronomique à faire en couple\n"
                                    "- Une machine à café personnalisée avec leurs initiales\n"
                                    "- Un coffret de vins ou spiritueux pour célébrer l’union\n"
                                    "- Un livre de recettes dédié aux repas romantiques\n"
                                    "- Une planche à découper gravée avec leurs noms\n"
                                    "- Un abonnement à une box culinaire pour tester des plats ensemble")))

    @Rule(Cadeau(age="25-40ans", sexe="masculin", interest="art", occasion="mariage"))
    def homme_mariage_art(self):
        self.declare(Resultat(result=("Pour un homme passionné d’art à l’occasion d’un mariage, voici des idées de cadeaux : \n"
                                    "- Une œuvre personnalisée représentant le couple ou une scène symbolique\n"
                                    "- Une sculpture en duo symbolisant l’union\n"
                                    "- Une peinture murale ou un tableau abstrait dédié à l’amour\n"
                                    "- Un atelier artistique à partager à deux (peinture, poterie, etc.)\n"
                                    "- Un album photo ou une série de portraits artistiques du couple\n"
                                    "- Une photographie encadrée en édition limitée\n"
                                    "- Une lampe ou un objet décoratif inspiré par un artiste célèbre\n"
                                    "- Un coffret ou un livre sur l’histoire de l’art lié au mariage")))
