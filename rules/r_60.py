from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

# subclass of InterfaceEngine
class InterfaceEngine_60ans(InterfaceEngine):
#femme------------------------------------------------------------------------------------------------------------------
#anniversaire
    @Rule(Cadeau(age="60plus", sexe="feminine", interest="livres", occasion="anniversaire"))
    def femme_60plus_anniversaire_livres(self):
        self.declare(Resultat(result=("Pour une femme d’âge mûr (60 ans et plus) passionnée de livres, voici des idées pour un anniversaire : \n"
                                  "- Une édition collector de son auteur préféré\n"
                                  "- Un abonnement à un club de lecture ou une box de livres mensuelle\n"
                                  "- Un livre de souvenirs personnalisé à remplir avec sa famille\n"
                                  "- Une lampe de lecture ergonomique\n"
                                  "- Un carnet de citations ou de pensées inspirantes\n"
                                  "- Un coffret thématique de littérature classique\n"
                                  "- Une liseuse électronique légère et facile à utiliser\n"
                                  "- Un livre illustré sur une thématique qu’elle aime (nature, voyages, art)")))
        
    @Rule(Cadeau(age="60plus", sexe="feminine", interest="confort", occasion="anniversaire"))
    def femme_60plus_anniversaire_confort(self):
        self.declare(Resultat(result=("Pour une femme d’âge mûr (60 ans et plus) recherchant le confort, voici des idées pour un anniversaire : \n"
                                  "- Un plaid en cachemire ou une couverture chauffante\n"
                                  "- Un fauteuil relax ergonomique\n"
                                  "- Des chaussons en laine de haute qualité\n"
                                  "- Une bouillotte design ou électrique\n"
                                  "- Un diffuseur d’huiles essentielles avec des arômes relaxants\n"
                                  "- Un coussin de lecture ou de soutien pour le dos\n"
                                  "- Une boîte à thé assortie avec des infusions apaisantes\n"
                                  "- Une robe de chambre élégante et confortable")))
        
    @Rule(Cadeau(age="60plus", sexe="feminine", interest="jardinage", occasion="anniversaire"))
    def femme_60plus_anniversaire_jardinage(self):
        self.declare(Resultat(result=("Pour une femme d’âge mûr (60 ans et plus) passionnée de jardinage, voici des idées pour son anniversaire : \n"
                                  "- Un set d’outils de jardinage ergonomiques et de qualité\n"
                                  "- Un livre illustré sur les plantes et les fleurs\n"
                                  "- Une décoration extérieure comme une statue ou une fontaine\n"
                                  "- Un kit pour créer un jardin aromatique ou floral\n"
                                  "- Une boîte à graines variées pour chaque saison\n"
                                  "- Un tablier de jardin avec des poches pratiques\n"
                                  "- Une serre compacte ou un kit pour jardiner en intérieur\n"
                                  "- Un abonnement à une revue spécialisée sur le jardinage")))
        
    @Rule(Cadeau(age="60plus", sexe="feminine", interest="jeux_de_société", occasion="anniversaire"))
    def femme_60plus_anniversaire_jeux(self):
        self.declare(Resultat(result=("Pour une femme d’âge mûr (60 ans et plus) passionnée de jeux de société, voici des idées pour son anniversaire : \n"
                                  "- Un jeu de société classique en édition de luxe (échecs, backgammon)\n"
                                  "- Un jeu de quiz ou de culture générale pour jouer en famille\n"
                                  "- Un jeu coopératif ou narratif adapté à ses goûts\n"
                                  "- Un jeu de cartes original ou artisanal\n"
                                  "- Un abonnement à un club ou à une box de jeux de société\n"
                                  "- Une table ou un support dédié aux jeux de société\n"
                                  "- Un livre sur l’histoire des jeux de société dans le monde\n"
                                  "- Un puzzle de qualité avec un motif artistique ou personnalisé")))
    # retraite
    @Rule(Cadeau(age="60plus", sexe="feminine", interest="livres", occasion="retraite"))
    def femme_60plus_retraite_livres_personnalise(self):
        self.declare(Resultat(result=("Pour une femme d’âge mûr (60 ans et plus) passionnée de livres et entrant en retraite, voici des idées plus personnalisées : \n"
                                  "- Une collection d’œuvres de son auteur préféré avec des éditions limitées ou dédicacées\n"
                                  "- Un livre personnalisé avec les souvenirs et anecdotes partagés par sa famille et ses amis\n"
                                  "- Un coffret cadeau comprenant un livre de développement personnel et un carnet pour planifier ses projets de retraite\n"
                                  "- Un abonnement à une plateforme de livres audio pour écouter des récits inspirants lors de ses moments de détente\n"
                                  "- Une liseuse électronique adaptée avec une bibliothèque déjà remplie de classiques\n"
                                  "- Un livre illustré sur ses passions (voyages, nature, art, etc.)\n"
                                  "- Un coffret premium de poésie ou de littérature pour explorer des genres nouveaux\n"
                                  "- Une masterclass d’écriture ou un cours de storytelling pour l’aider à écrire ses mémoires")))
        
    @Rule(Cadeau(age="60plus", sexe="feminine", interest="confort", occasion="retraite"))
    def femme_60plus_retraite_confort_personnalise(self):
        self.declare(Resultat(result=("Pour une femme d’âge mûr (60 ans et plus) cherchant du confort et célébrant sa retraite, voici des propositions : \n"
                                  "- Un fauteuil inclinable haut de gamme, idéal pour la lecture ou les siestes\n"
                                  "- Un abonnement à un service de spa à domicile ou des soins relaxants\n"
                                  "- Une couverture pondérée pour des nuits paisibles\n"
                                  "- Un diffuseur d’arômes intelligent avec des huiles relaxantes personnalisées\n"
                                  "- Un panier cadeau composé de thés, infusions et accessoires de bien-être\n"
                                  "- Une robe de chambre luxueuse et des chaussons assortis\n"
                                  "- Un oreiller ergonomique pour lire confortablement au lit\n"
                                  "- Un abonnement à un programme de relaxation guidée ou de méditation spécialement conçu pour les seniors")))
        
    @Rule(Cadeau(age="60plus", sexe="feminine", interest="jardinage", occasion="retraite"))
    def femme_60plus_retraite_jardinage_personnalise(self):
        self.declare(Resultat(result=("Pour une femme d’âge mûr (60 ans et plus) passionnée de jardinage entrant en retraite, voici des idées plus personnelles : \n"
                                  "- Un atelier ou cours de jardinage pour perfectionner ses techniques\n"
                                  "- Une table de rempotage personnalisée avec son nom gravé\n"
                                  "- Un set d’outils de jardinage ergonomiques avec des poignées adaptées\n"
                                  "- Une décoration extérieure unique, comme une sculpture ou une fontaine\n"
                                  "- Un guide spécialisé sur les jardins médicinaux ou les plantes bio\n"
                                  "- Une collection de pots en céramique peints à la main\n"
                                  "- Une serre compacte ou un mini-potager vertical pour l’intérieur\n"
                                  "- Un carnet de jardinage élégant pour documenter ses plantations et leurs évolutions")))
        
    @Rule(Cadeau(age="60plus", sexe="feminine", interest="jeux_de_société", occasion="retraite"))
    def femme_60plus_retraite_jeux_personnalise(self):
        self.declare(Resultat(result=("Pour une femme d’âge mûr (60 ans et plus) aimant les jeux de société, voici des idées adaptées à sa retraite : \n"
                                  "- Un jeu de société familial personnalisé avec des anecdotes ou photos marquantes\n"
                                  "- Une édition de luxe d’un classique (échecs, dames, Scrabble)\n"
                                  "- Un abonnement à des rencontres mensuelles de jeux pour seniors dans sa région\n"
                                  "- Un jeu coopératif favorisant des moments partagés avec ses petits-enfants\n"
                                  "- Un kit de fabrication de puzzle personnalisé avec des photos de famille\n"
                                  "- Une mallette élégante pour ranger ses jeux préférés\n"
                                  "- Un jeu d’évasion à domicile, pour s’amuser avec sa famille\n"
                                  "- Un cours en ligne ou un atelier sur des stratégies avancées de jeux qu’elle apprécie")))

#homme------------------------------------------------------------------------------------------------------------------
#anniversaire
    @Rule(Cadeau(age="60plus", sexe="masculin", interest="livres", occasion="anniversaire"))
    def homme_60plus_anniversaire_livres(self):
        self.declare(Resultat(result=("Pour un homme d’âge mûr (60 ans et plus) passionné de livres, voici des idées adaptées pour son anniversaire : \n"
                                  "- Une biographie inspirante ou un récit historique captivant\n"
                                  "- Une édition spéciale d’un classique littéraire qu’il aime\n"
                                  "- Un abonnement à un magazine ou journal spécialisé dans ses passions (sport, histoire, etc.)\n"
                                  "- Un coffret de livres sur des thèmes qu’il apprécie (voyage, philosophie, aventure)\n"
                                  "- Un guide illustré sur un hobby, comme la pêche ou le bricolage\n"
                                  "- Une liseuse électronique préchargée avec ses genres favoris\n"
                                  "- Une lampe de lecture élégante et pratique pour les longues soirées de lecture\n"
                                  "- Un carnet pour écrire ses propres souvenirs ou pensées inspirées par ses lectures")))
        
    @Rule(Cadeau(age="60plus", sexe="masculin", interest="confort", occasion="anniversaire"))
    def homme_60plus_anniversaire_confort(self):
        self.declare(Resultat(result=("Pour un homme d’âge mûr (60 ans et plus) qui recherche le confort à l’occasion de son anniversaire : \n"
                                  "- Un fauteuil ergonomique ou un repose-pieds massant\n"
                                  "- Une couverture chauffante ou une couverture pondérée\n"
                                  "- Une paire de chaussons en cuir ou un peignoir en coton haut de gamme\n"
                                  "- Un oreiller à mémoire de forme pour un confort optimal\n"
                                  "- Un plaid personnalisé avec ses initiales\n"
                                  "- Un coffret bien-être comprenant des huiles essentielles et un diffuseur\n"
                                  "- Une machine à café premium pour savourer de bons moments de détente\n"
                                  "- Une paire de lunettes de repos ou un support pour tablette pour ses lectures ou séries")))
        
    @Rule(Cadeau(age="60plus", sexe="masculin", interest="jardinage", occasion="anniversaire"))
    def homme_60plus_anniversaire_jardinage(self):
        self.declare(Resultat(result=("Pour un homme d’âge mûr (60 ans et plus) passionné de jardinage, voici des idées cadeaux pour son anniversaire : \n"
                                  "- Une mallette d’outils de jardinage haut de gamme avec gravure personnalisée\n"
                                  "- Une station météo connectée pour surveiller ses plantations\n"
                                  "- Une chaise ou un tabouret de jardin pliable avec rangement intégré\n"
                                  "- Une serre de jardin compacte ou un potager surélevé\n"
                                  "- Un guide pratique sur l'entretien des plantes rares ou des arbres fruitiers\n"
                                  "- Un chapeau de jardinage élégant avec protection UV\n"
                                  "- Une fontaine d’extérieur ou une sculpture pour embellir son espace vert\n"
                                  "- Un abonnement à un club de jardinage ou des ateliers pratiques près de chez lui")))
    
    @Rule(Cadeau(age="60plus", sexe="masculin", interest="jeux_de_société", occasion="anniversaire"))
    def homme_60plus_anniversaire_jeux(self):
        self.declare(Resultat(result=("Pour un homme d’âge mûr (60 ans et plus) amateur de jeux de société, voici des idées cadeaux adaptées à son anniversaire : \n"
                                  "- Une édition collector d’un jeu classique comme les échecs ou le Monopoly\n"
                                  "- Un jeu de société stratégique adapté aux adultes comme Catan ou Carcassonne\n"
                                  "- Un jeu de cartes personnalisé avec des thématiques qu’il aime\n"
                                  "- Une table ou un coffret de rangement élégant pour ses jeux\n"
                                  "- Un abonnement à une ludothèque locale pour découvrir de nouveaux jeux\n"
                                  "- Un puzzle complexe ou 3D représentant un lieu historique ou un paysage qu’il aime\n"
                                  "- Une mallette de poker complète pour jouer entre amis ou en famille\n"
                                  "- Un jeu d'évasion ou de rôle à faire avec ses proches lors de soirées conviviales")))
    
# retraite
    @Rule(Cadeau(age="60plus", sexe="masculin", interest="livres", occasion="retraite"))
    def homme_60plus_retraite_livres(self):
        self.declare(Resultat(result=("Pour un homme d’âge mûr (60 ans et plus) passionné de livres à l'occasion de sa retraite : \n"
                                    "- Une collection spéciale d'œuvres littéraires classiques ou d’un auteur qu’il apprécie\n"
                                    "- Un atlas ou un livre illustré sur les voyages et paysages du monde\n"
                                    "- Un guide sur la retraite et les loisirs pour cette nouvelle étape\n"
                                    "- Une biographie d’un personnage inspirant ou historique\n"
                                    "- Un abonnement à un magazine sur ses centres d’intérêt (nature, histoire, etc.)\n"
                                    "- Une liseuse électronique avec une sélection de livres préchargés\n"
                                    "- Une étagère design ou un support élégant pour exposer ses livres préférés\n"
                                    "- Un carnet de notes ou journal pour écrire ses mémoires ou ses réflexions de retraite")))
        
    @Rule(Cadeau(age="60plus", sexe="masculin", interest="jardinage", occasion="retraite"))
    def homme_60plus_retraite_jardinage(self):
        self.declare(Resultat(result=("Pour un homme d’âge mûr (60 ans et plus) passionné de jardinage célébrant sa retraite : \n"
                                    "- Un ensemble d’outils de jardinage haut de gamme avec poignée ergonomique\n"
                                    "- Une petite serre ou un potager d'intérieur pour cultiver des plantes toute l'année\n"
                                    "- Un guide sur les plantes exotiques ou l'entretien des bonsaïs\n"
                                    "- Une tonnelle ou un parasol pour créer un coin détente dans son jardin\n"
                                    "- Un kit pour créer un jardin japonais ou zen\n"
                                    "- Une station météo connectée pour surveiller le climat de son jardin\n"
                                    "- Des graines rares ou des plants d’arbres fruitiers pour un projet à long terme\n"
                                    "- Une fontaine de jardin ou un système d’éclairage décoratif pour embellir son espace extérieur")))

    @Rule(Cadeau(age="60plus", sexe="masculin", interest="jeux_de_société", occasion="retraite"))
    def homme_60plus_retraite_jeux(self):
        self.declare(Resultat(result=("Pour un homme d’âge mûr (60 ans et plus) amateur de jeux de société à l'occasion de sa retraite : \n"
                                    "- Une édition de luxe d’un jeu de plateau classique, comme les échecs ou le backgammon\n"
                                    "- Un jeu stratégique ou collaboratif adapté aux adultes, comme Terraforming Mars\n"
                                    "- Un jeu de cartes personnalisé avec des thématiques qui lui plaisent\n"
                                    "- Un coffret de poker haut de gamme avec des jetons en céramique\n"
                                    "- Un abonnement à une ludothèque ou des soirées de jeux près de chez lui\n"
                                    "- Une table pliante spécialement conçue pour les jeux de société\n"
                                    "- Un puzzle complexe ou en 3D représentant un monument ou un lieu symbolique\n"
                                    "- Un jeu de rôle ou un escape game pour partager des moments en famille ou entre amis")))
