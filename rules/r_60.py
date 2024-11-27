from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

# subclass of InterfaceEngine
class InterfaceEngine_60ans(InterfaceEngine):
#femme------------------------------------------------------------------------------------------------------------------
#anniversaire
    @Rule(Cadeau(age="60plus", sexe="feminine", interest="livres", occasion="anniversaire"))
    def femme_60plus_anniversaire_livres(self):
        self.declare(Resultat(result=("Pour une femme de 60 ans et plus passionnée de livres, voici des idées pour un anniversaire : \n"
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
        self.declare(Resultat(result=("Pour une femme de 60 ans et plus recherchant le confort, voici des idées pour un anniversaire : \n"
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
        self.declare(Resultat(result=("Pour une femme passionnée de jardinage, voici des idées pour son anniversaire : \n"
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
        self.declare(Resultat(result=("Pour une femme passionnée de jeux de société, voici des idées pour son anniversaire : \n"
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
        self.declare(Resultat(result=("Pour une femme passionnée de livres et entrant en retraite, voici des idées plus personnalisées : \n"
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
        self.declare(Resultat(result=("Pour une femme cherchant du confort et célébrant sa retraite, voici des propositions : \n"
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
        self.declare(Resultat(result=("Pour une femme passionnée de jardinage entrant en retraite, voici des idées plus personnelles : \n"
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
        self.declare(Resultat(result=("Pour une femme aimant les jeux de société, voici des idées adaptées à sa retraite : \n"
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

    



