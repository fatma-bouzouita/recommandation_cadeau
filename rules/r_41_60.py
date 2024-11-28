from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

# subclass of InterfaceEngine
class InterfaceEngine_41_60ans(InterfaceEngine):
    #femme------------------------------------------------------------------------------------------------------------------
    #anniversaire
    @Rule(Cadeau(age="41_60ans", sexe="feminine", interest="jardinage", occasion="anniversaire"))
    def femme_anniversaire_jardinage(self):
        self.declare(Resultat(result=("Pour une femme aimant le jardinage, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un ensemble d'outils de jardinage ergonomiques (sécateur, pelle, râteau, etc.) \n"
                                        "- Un tablier de jardinage personnalisé avec des poches pratiques \n"
                                        "- Une serre en kit pour cultiver des plantes toute l’année \n"
                                        "- Des graines ou des bulbes de fleurs rares ou exotiques \n"
                                        "- Un kit de jardinage en intérieur pour cultiver des herbes aromatiques \n"
                                        "- Un composteur compact pour recycler les déchets organiques \n"
                                        "- Un arrosoir design ou une fontaine décorative pour le jardin")))

    @Rule(Cadeau(age="41_60ans", sexe="feminine", interest="décoration", occasion="anniversaire"))
    def femme_anniversaire_décoration(self):
        self.declare(Resultat(result=("Pour une femme aimant la décoration, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un vase design ou artisanal pour embellir son intérieur \n"
                                        "- Des coussins décoratifs aux motifs élégants ou personnalisés \n"
                                        "- Une lampe d’ambiance ou une guirlande lumineuse pour créer une atmosphère chaleureuse \n"
                                        "- Un cadre photo ou un tableau mural moderne pour habiller ses murs \n"
                                        "- Des bougies parfumées ou un diffuseur d'huiles essentielles avec un design épuré \n"
                                        "- Un miroir décoratif ou un miroir rond avec une bordure en bois ou en métal \n"
                                        "- Une horloge murale unique ou vintage pour une touche d’élégance \n"
                                        "- Des plantes d’intérieur avec des pots assortis pour ajouter une touche de verdure")))

    @Rule(Cadeau(age="41_60ans", sexe="feminine", interest="voyage", occasion="anniversaire"))
    def femme_anniversaire_voyage(self):
        self.declare(Resultat(result=("Pour une femme aimant le voyage, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Une valise élégante et légère avec des compartiments pratiques \n"
                                        "- Un sac à dos de voyage ergonomique et stylé \n"
                                        "- Un journal de voyage personnalisé pour noter ses aventures \n"
                                        "- Une carte du monde à gratter pour suivre ses destinations visitées \n"
                                        "- Un guide de voyage sur des destinations de rêve \n"
                                        "- Une trousse de toilette compacte et compartimentée \n"
                                        "- Un oreiller de voyage ergonomique pour les longs trajets \n"
                                        "- Un appareil photo instantané pour capturer des souvenirs uniques")))

    @Rule(Cadeau(age="41_60ans", sexe="feminine", interest="cuisine", occasion="anniversaire"))
    def femme_anniversaire_cuisine(self):
        self.declare(Resultat(result=("Pour une femme aimant la cuisine, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un robot culinaire multifonction pour faciliter la préparation des repas \n"
                                        "- Un coffret d'épices rares et exotiques pour expérimenter de nouvelles saveurs \n"
                                        "- Un livre de recettes de chefs célèbres ou sur une cuisine spécifique (italienne, japonaise, etc.) \n"
                                        "- Un set de couteaux professionnels avec un bloc de rangement \n"
                                        "- Des ustensiles de pâtisserie pour créer des desserts gourmands (moules, douilles, spatules) \n"
                                        "- Un tablier personnalisé avec son nom ou un message inspirant \n"
                                        "- Un cours de cuisine en ligne ou en présentiel avec un chef \n"
                                        "- Une cocotte en fonte ou un plat de cuisson de haute qualité")))

    @Rule(Cadeau(age="41_60ans", sexe="feminine", interest="livres", occasion="anniversaire"))
    def femme_anniversaire_livres(self):
        self.declare(Resultat(result=("Pour une femme aimant les livres, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Une édition collector ou illustrée de son livre préféré \n"
                                        "- Un abonnement à une box mensuelle de livres selon ses goûts littéraires \n"
                                        "- Un marque-page artisanal ou personnalisé en métal, cuir ou bois \n"
                                        "- Une liseuse électronique pour lire où qu’elle soit avec une grande bibliothèque \n"
                                        "- Un carnet de lecture pour noter ses impressions et ses livres à lire \n"
                                        "- Un set de livres inspirants ou motivants sur le développement personnel \n"
                                        "- Un ouvrage de cuisine, de voyage ou de décoration selon ses centres d’intérêt secondaires")))

    @Rule(Cadeau(age="41_60ans", sexe="feminine", interest="jeux_de_société", occasion="anniversaire"))
    def femme_anniversaire_jeux_de_société(self):
        self.declare(Resultat(result=("Pour une femme aimant les jeux de société, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un jeu de société stratégique comme **Catan**, **Ticket to Ride** ou **Carcassonne** \n"
                                        "- Un jeu de société coopératif, tel que **Pandemic** ou **Les Aventuriers du Rail** \n"
                                        "- Un jeu de société d'ambiance pour des soirées entre amis, comme **Dixit**, **Codenames** ou **Time's Up** \n"
                                        "- Un jeu de société avec des mécaniques innovantes comme **Azul** ou **Terraforming Mars** \n"
                                        "- Un puzzle complexe ou un casse-tête en bois pour stimuler l'esprit \n"
                                        "- Un abonnement à une box mensuelle de jeux de société pour découvrir de nouveaux jeux chaque mois \n"
                                        "- Un livre ou un guide sur les stratégies de jeux de société pour améliorer ses compétences")))

    @Rule(Cadeau(age="41_60ans", sexe="feminine", interest="mode", occasion="anniversaire"))
    def femme_anniversaire_mode(self):
        self.declare(Resultat(result=("Pour une femme aimant la mode, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un sac à main de créateur ou une marque tendance \n"
                                    "- Une écharpe en cachemire ou un foulard en soie de qualité \n"
                                    "- Des bijoux fins et élégants (bracelets, boucles d'oreilles, colliers) \n"
                                    "- Un ensemble de vêtements stylés (robe chic, tailleur élégant, ou vêtements à la mode) \n"
                                    "- Un abonnement à une box mode pour découvrir de nouvelles tendances chaque mois \n"
                                    "- Une paire de chaussures de créateur ou des baskets tendances \n"
                                    "- Un parfum haut de gamme ou une bougie parfumée de luxe \n"
                                    "- Un porte-cartes ou un portefeuille en cuir de qualité")))

    #femme------------------------------------------------------------------------------------------------------------------
    #Retraite
    @Rule(Cadeau(age="41_60ans", sexe="feminine", interest="jardinage", occasion="retraite"))
    def femme_retraite_jardinage(self):
        self.declare(Resultat(result=("Pour une femme aimant le jardinage, voici des idées de cadeaux pour sa retraite : \n"
                                        "- Une lampe solaire pour éclairer son jardin de manière écologique \n"
                                        "- Des livres ou guides sur le jardinage et l’entretien des plantes \n"
                                        "- Une chaise longue ou un banc de jardin pour se détendre dans son espace vert \n"
                                        "- Des gants de jardinage résistants et élégants \n"
                                        "- Un atelier ou un cours sur la création de jardins ou d’arrangements floraux \n"
                                        "- Des décorations pour le jardin, comme des statues, des lanternes ou des carillons \n"
                                        "- Un calendrier ou une application de jardinage pour planifier les semis et récoltes \n"
                                        "- Une jardinière ou un pot design pour mettre en valeur ses plantations.")))

    @Rule(Cadeau(age="41_60ans", sexe="feminine", interest="décoration", occasion="retraite"))
    def femme_retraite_décoration(self):
        self.declare(Resultat(result=("Pour une femme aimant la décoration, voici des idées de cadeaux pour sa retraite : \n"
                                        "- Une nappe ou des sets de table stylés pour agrémenter sa table à manger \n"
                                        "- Un tapis tendance ou une peau de mouton pour apporter du confort à son espace \n"
                                        "- Des rideaux ou des voilages avec des motifs qui s’accordent avec son style intérieur \n"
                                        "- Une boîte à bijoux ou un organisateur de bureau esthétique \n"
                                        "- Un abonnement à un magazine de décoration pour suivre les tendances \n"
                                        "- Une œuvre d’art ou une sculpture pour une pièce maîtresse unique \n"
                                        "- Un atelier ou un cours pour apprendre à réaliser des objets de décoration faits maison.")))

    @Rule(Cadeau(age="41_60ans", sexe="feminine", interest="voyage", occasion="retraite"))
    def femme_retraite_voyage(self):
        self.declare(Resultat(result=("Pour une femme aimant le voyage, voici des idées de cadeaux pour sa retraite : \n"
                                        "- Une pochette de passeport avec un design chic et fonctionnel \n"
                                        "- Un abonnement à un service de streaming de documentaires de voyage \n"
                                        "- Des accessoires de voyage comme des étiquettes à bagages personnalisées \n"
                                        "- Une couverture légère et pliable pour les voyages en avion ou en train \n"
                                        "- Un chargeur portable pour rester connectée pendant ses escapades \n"
                                        "- Une expérience de voyage comme un séjour en spa, une nuit insolite, ou un city tour \n"
                                        "- Un coffret cadeau avec des bons pour des excursions ou des activités locales.")))

    @Rule(Cadeau(age="41_60ans", sexe="feminine", interest="cuisine", occasion="retraite"))
    def femme_retraite_cuisine(self):
        self.declare(Resultat(result=("Pour une femme aimant la cuisine, voici des idées de cadeaux pour sa retraite : \n"
                                        "- Une planche à découper en bois gravée avec un design unique \n"
                                        "- Un kit de fabrication maison (ex. fromage, chocolat, pâtes fraîches) \n"
                                        "- Une machine à café ou un accessoire pour préparer des boissons chaudes sophistiquées \n"
                                        "- Un extracteur de jus pour des préparations saines et naturelles \n"
                                        "- Des bols de préparation en céramique ou un set de vaisselle coloré \n"
                                        "- Une carte cadeau pour un magasin spécialisé en matériel de cuisine \n"
                                        "- Un abonnement à un service de livraison de box de cuisine ou de produits gastronomiques.")))

    @Rule(Cadeau(age="41_60ans", sexe="feminine", interest="livres", occasion="retraite"))
    def femme_retraite_livres(self):
        self.declare(Resultat(result=("Pour une femme aimant les livres, voici des idées de cadeaux pour sa retraite : \n"
                                        "- Un fauteuil ou un coussin de lecture confortable pour créer un coin lecture parfait \n"
                                        "- Une lampe de lecture rechargeable et ajustable pour lire sans déranger \n"
                                        "- Une bibliothèque originale ou un rangement design pour ses livres \n"
                                        "- Des romans récents ou des best-sellers dans ses genres préférés (policier, romance, fantastique) \n"
                                        "- Une carte cadeau pour une librairie locale ou en ligne \n"
                                        "- Un cours ou atelier d'écriture pour développer sa créativité littéraire \n"
                                        "- Un agenda ou un calendrier littéraire avec des citations et des recommandations.")))

    @Rule(Cadeau(age="41_60ans", sexe="feminine", interest="jeux_de_société", occasion="retraite"))
    def femme_anniversaire_jeux_de_société(self):
        self.declare(Resultat(result=("Pour une femme aimant les jeux de société, voici des idées de cadeaux pour sa retraite : \n"
                                        "- Un porte-cartes ou un organiser pour ranger et protéger ses jeux de société \n"
                                        "- Un jeu de société personnalisé avec ses propres règles ou thème préféré \n"
                                        "- Un tapis de jeu de qualité pour améliorer l’expérience de jeu \n"
                                        "- Un accessoire comme un minuteur de jeu ou des jetons spéciaux pour personnaliser ses parties \n"
                                        "- Une soirée privée dans un café de jeux de société local pour découvrir de nouveaux jeux \n"
                                        "- Un set de jeux de cartes comme **Uno**, **Poker**, ou **Cards Against Humanity** \n"
                                        "- Un jeu éducatif ou culturel pour enrichir ses connaissances tout en s'amusant.")))

    @Rule(Cadeau(age="41_60ans", sexe="feminine", interest="mode", occasion="retraite"))
    def femme_retraite_mode(self):
        self.declare(Resultat(result=("Pour une femme aimant la mode, voici des idées de cadeaux pour sa retraite : \n"
                                    "- Un abonnement à un magazine de mode pour suivre les dernières tendances \n"
                                    "- Un vêtement personnalisé avec ses initiales ou un motif unique \n"
                                    "- Une séance de shopping avec un styliste personnel \n"
                                    "- Un vêtement ou accessoire de mode éthique ou écoresponsable \n"
                                    "- Un bijou personnalisé gravé avec un message spécial \n"
                                    "- Une montre élégante ou un bracelet montre pour compléter son look.")))

    #homme------------------------------------------------------------------------------------------------------------------
    #anniversaire
    @Rule(Cadeau(age="41_60ans", sexe="masculin", interest="jardinage", occasion="anniversaire"))
    def homme_anniversaire_jardinage(self):
        self.declare(Resultat(result=("Pour un homme aimant le jardinage, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un kit complet d'outils de jardinage (bêche, sécateur, râteau, etc.) \n"
                                        "- Des gants de jardinage de haute qualité et confortables \n"
                                        "- Un fauteuil de jardin ou une chaise longue pour se détendre dans son jardin \n"
                                        "- Des plantes en pot ou des fleurs rares à ajouter à son jardin \n"
                                        "- Un composteur pour recycler les déchets organiques et nourrir son jardin \n"
                                        "- Une fontaine de jardin ou un bassin pour ajouter une touche de sérénité \n"
                                        "- Un abonnement à un magazine de jardinage pour des conseils et des idées")))

    @Rule(Cadeau(age="41_60ans", sexe="masculin", interest="décoration", occasion="anniversaire"))
    def homme_anniversaire_décoration(self):
        self.declare(Resultat(result=("Pour un homme aimant la décoration, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Une horloge murale design ou vintage pour embellir une pièce \n"
                                        "- Un tableau ou une œuvre d'art personnalisée correspondant à ses goûts \n"
                                        "- Une lampe de designer ou une lampe d'ambiance originale \n"
                                        "- Des coussins décoratifs ou un plaid élégant pour le salon \n"
                                        "- Un miroir moderne ou au style rétro pour un effet d'agrandissement \n"
                                        "- Un vase ou une sculpture contemporaine pour la table ou les étagères \n"
                                        "- Une bibliothèque ou une étagère murale au design unique \n")))

    @Rule(Cadeau(age="41_60ans", sexe="masculin", interest="voyage", occasion="anniversaire"))
    def homme_anniversaire_voyage(self):
        self.declare(Resultat(result=("Pour un homme aimant le voyage, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Une valise légère et robuste ou un sac de voyage élégant \n"
                                        "- Une carte du monde à gratter pour marquer les destinations visitées \n"
                                        "- Un guide de voyage pour sa prochaine destination ou une destination inspirante \n"
                                        "- Une trousse de toilette compacte et bien organisée pour les déplacements \n"
                                        "- Un adaptateur universel pour ses voyages à l'étranger \n"
                                        "- Un oreiller de voyage ergonomique et confortable \n"
                                        "- Un carnet de voyage personnalisé pour noter ses souvenirs \n"
                                        "- Une gourde réutilisable ou une bouteille filtrante pour les aventuriers")))

    @Rule(Cadeau(age="41_60ans", sexe="masculin", interest="cuisine", occasion="anniversaire"))
    def homme_anniversaire_cuisine(self):
        self.declare(Resultat(result=("Pour un homme aimant la cuisine, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un ensemble de couteaux de cuisine haut de gamme ou personnalisés \n"
                                        "- Un tablier élégant et personnalisé avec son prénom ou une citation amusante \n"
                                        "- Une planche à découper en bois de qualité avec un design unique \n"
                                        "- Un kit pour préparer des plats spécifiques (ex. kit à sushi, kit à barbecue) \n"
                                        "- Un livre de recettes sur son type de cuisine préféré (ex. cuisine italienne, asiatique) \n"
                                        "- Un cours de cuisine en ligne ou en présentiel avec un chef professionnel \n"
                                        "- Une cocotte ou un faitout en fonte de haute qualité")))

    @Rule(Cadeau(age="41_60ans", sexe="masculin", interest="livres", occasion="anniversaire"))
    def homme_anniversaire_livres(self):
        self.declare(Resultat(result=("Pour un homme aimant les livres, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Une collection complète de son auteur préféré ou un livre rare \n"
                                        "- Un abonnement à un service de lecture numérique (ex. Kindle Unlimited, Audible) \n"
                                        "- Un marque-page personnalisé ou artisanal \n"
                                        "- Un livre sur un sujet qui le passionne (histoire, science, voyage, philosophie) \n"
                                        "- Un coffret de beaux livres illustrés sur l'art, la photographie, ou la nature \n"
                                        "- Un agenda ou carnet de notes élégant pour un amateur de lecture et d'écriture \n"
                                        "- Une liseuse électronique (si elle n'est pas déjà en sa possession) \n")))

    @Rule(Cadeau(age="41_60ans", sexe="masculin", interest="jeux_de_société", occasion="anniversaire"))
    def homme_anniversaire_jeux_de_société(self):
        self.declare(Resultat(result=("Pour un homme aimant les jeux de société, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Une version premium ou collector de son jeu de société préféré \n"
                                        "- Un nouveau jeu de société tendance ou classique (ex. Catan, Carcassonne, Azul) \n"
                                        "- Un jeu d'échecs ou de dames en bois sculpté pour un style élégant \n"
                                        "- Un ensemble de jeux de société pour deux joueurs, parfait pour des soirées à deux \n"
                                        "- Une table de jeux avec des compartiments pour ranger les accessoires \n"
                                        "- Un livre ou guide sur les stratégies pour les jeux qu'il aime \n"
                                        "- Des accessoires personnalisés comme des dés uniques ou des pions en métal")))

    @Rule(Cadeau(age="41_60ans", sexe="masculin", interest="mode", occasion="anniversaire"))
    def homme_anniversaire_mode(self):
        self.declare(Resultat(result=("Pour un homme aimant la mode, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Une montre élégante adaptée à son style (classique, moderne ou sportif) \n"
                                        "- Un ensemble de cravates, nœuds papillon ou boutons de manchette haut de gamme \n"
                                        "- Une chemise sur mesure ou une veste en cuir de qualité \n"
                                        "- Des chaussures tendance, comme des mocassins, sneakers ou bottines \n"
                                        "- Un portefeuille ou une ceinture en cuir véritable \n"
                                        "- Une sacoche pour un look chic et pratique \n"
                                        "- Un abonnement à une box de vêtements ou accessoires de mode \n"
                                        "- Un parfum raffiné qui reflète sa personnalité")))

    #homme------------------------------------------------------------------------------------------------------------------
    #retraite
    @Rule(Cadeau(age="41_60ans", sexe="masculin", interest="jardinage", occasion="retraite"))
    def homme_retraite_jardinage(self):
        self.declare(Resultat(result=("Pour un homme aimant le jardinage, voici des idées de cadeaux pour sa retraite : \n"
                                        "- Un livre spécialisé sur le jardinage ou l'horticulture \n"
                                        "- Des graines de plantes ou d'arbres à cultiver dans son jardin \n"
                                        "- Un système d'arrosage automatique ou un tuyau extensible \n"
                                        "- Un banc de jardin confortable ou une table de pique-nique \n"
                                        "- Une serre de jardin pour cultiver des plantes délicates ou des légumes \n"
                                        "- Des accessoires décoratifs pour le jardin comme des statues, des lanternes ou des guirlandes lumineuses \n"
                                        "- Un kit de culture en intérieur pour cultiver des herbes fraîches toute l'année.")))

    @Rule(Cadeau(age="41_60ans", sexe="masculin", interest="décoration", occasion="retraite"))
    def homme_retraite_décoration(self):
        self.declare(Resultat(result=("Pour un homme aimant la décoration, voici des idées de cadeaux pour sa retraite : \n"
                                        "- Des cadres photo personnalisés pour afficher des souvenirs précieux \n"
                                        "- Un terrarium ou un ensemble de plantes décoratives d'intérieur \n"
                                        "- Un diffuseur d'huiles essentielles au design épuré pour l'aromathérapie \n"
                                        "- Un tapis élégant pour ajouter une touche de confort et de style \n"
                                        "- Un porte-revues ou un organisateur mural pratique et esthétique \n"
                                        "- Une lampe ou un luminaire intelligent contrôlé par une application \n"
                                        "- Des accessoires de décoration sur un thème qu'il apprécie (nature, voyages, minimalisme, etc.).")))

    @Rule(Cadeau(age="41_60ans", sexe="masculin", interest="voyage", occasion="retraite"))
    def homme_retraite_voyage(self):
        self.declare(Resultat(result=("Pour un homme aimant le voyage, voici des idées de cadeaux pour sa retraite : \n"
                                        "- Un abonnement à une box de découverte culturelle (ex. cuisine du monde) \n"
                                        "- Des gadgets pratiques comme une batterie externe puissante ou un tracker GPS \n"
                                        "- Une caméra d'action ou un drone compact pour immortaliser ses voyages \n"
                                        "- Une expérience de voyage unique comme un vol en montgolfière ou une excursion \n"
                                        "- Des accessoires pour voyager en toute sérénité, comme des écouteurs anti-bruit ou un masque de sommeil \n"
                                        "- Un abonnement à une application de voyage ou à un magazine spécialisé dans le tourisme.")))

    @Rule(Cadeau(age="41_60ans", sexe="masculin", interest="cuisine", occasion="retraite"))
    def homme_retraite_cuisine(self):
        self.declare(Resultat(result=("Pour un homme aimant la cuisine, voici des idées de cadeaux pour sa retraite : \n"
                                        "- Des épices rares ou un coffret d'huiles d'olive aromatisées \n"
                                        "- Un appareil de cuisine innovant comme un robot multifonction ou une machine sous vide \n"
                                        "- Un abonnement à une box culinaire pour découvrir de nouveaux produits chaque mois \n"
                                        "- Un thermomètre de cuisine numérique ou un chalumeau de cuisine pour les finitions \n"
                                        "- Des moules ou ustensiles pour des pâtisseries créatives \n"
                                        "- Un set de verres à vin ou un décanteur pour accompagner ses repas \n"
                                        "- Une pierre à pizza ou un four à pizza portable pour des soirées conviviales.")))

    @Rule(Cadeau(age="41_60ans", sexe="masculin", interest="livres", occasion="retraite"))
    def homme_retraite_livres(self):
        self.declare(Resultat(result=("Pour un homme aimant les livres, voici des idées de cadeaux pour sa retraite : \n"
                                        "- Une lampe de lecture flexible et rechargeable pour lire confortablement la nuit \n"
                                        "- Un abonnement à une box livresque qui propose des livres surprises chaque mois \n"
                                        "- Un atlas ou un guide de voyage pour inspirer ses prochaines aventures \n"
                                        "- Un livre avec des dédicaces ou des éditions limitées \n"
                                        "- Une étagère de design original pour mettre en valeur sa collection de livres \n"
                                        "- Des livres de développement personnel ou de business, s'il s'y intéresse \n"
                                        "- Une carte cadeau dans sa librairie préférée pour qu'il choisisse lui-même ses lectures.")))

    @Rule(Cadeau(age="41_60ans", sexe="masculin", interest="jeux_de_société", occasion="retraite"))
    def homme_retraite_jeux_de_société(self):
        self.declare(Resultat(result=("Pour un homme aimant les jeux de société, voici des idées de cadeaux pour sa retraite : \n"
                                        "- Une boîte de rangement ou un organiseur pour ses jeux de société \n"
                                        "- Un abonnement à des événements ou soirées de jeux dans sa région \n"
                                        "- Une box découverte mensuelle de nouveaux jeux de société \n"
                                        "- Des jeux de cartes modernes ou classiques (ex. Uno, 7 Wonders, Hanabi) \n"
                                        "- Un tapis de jeu ou une nappe thématique pour des parties immersives \n"
                                        "- Une application compagnon pour jeux de société, si disponible pour ses jeux favoris \n"
                                        "- Des extensions pour ses jeux existants, offrant de nouvelles aventures et défis.")))

    @Rule(Cadeau(age="41_60ans", sexe="masculin", interest="mode", occasion="retraite"))
    def homme_retraite_mode(self):
        self.declare(Resultat(result=("Pour un homme aimant la mode, voici des idées de cadeaux pour sa retraite : \n"
                                        "- Un sac à main de créateur ou une marque tendance \n"
                                        "- Une paire de lunettes de soleil design ou des lunettes à monture stylée \n"
                                        "- Un ensemble de soins pour barbe ou cheveux, pour compléter son style \n"
                                        "- Un foulard ou une écharpe de marque pour les saisons fraîches \n"
                                        "- Une carte cadeau pour une boutique de mode qu'il aime \n"
                                        "- Des accessoires modernes, comme une casquette, un chapeau ou une écharpe trendy \n"
                                        "- Une consultation avec un styliste personnel ou une session de shopping assistée.")))
