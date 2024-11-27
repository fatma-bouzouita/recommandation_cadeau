from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

# subclass of InterfaceEngine
class InterfaceEngine_41_30ans(InterfaceEngine):
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
