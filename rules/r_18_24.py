from experta import Rule
from models.facts import Cadeau, Resultat
from models.engine_base import InterfaceEngine

# subclass of InterfaceEngine
class InterfaceEngine_18_24ans(InterfaceEngine):
    #fille------------------------------------------------------------------------------------------------------------------
    #anniversaire
    @Rule(Cadeau(age="18-24ans", sexe="feminine", interest="mode", occasion="anniversaire"))
    def fille_anniversaire_mode(self):
        self.declare(Resultat(result=("Pour une jeune femme adulte aimant la mode, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Une montre \n"
                                        "- Une paire de lunettes de soleil stylées \n"
                                        "- Un parfum de marque avec une senteur moderne \n"
                                        "- Un sac à main design ou une pochette chic \n"
                                        "- Un coffret de maquillage de marques populaires \n"
                                        "- Une carte cadeau dans une boutique de mode \n"
                                        "- Un kit de soins pour la peau \n"
                                        "- Un bijou (bracelet, collier, boucles d'oreilles) \n"
                                        "- Une écharpe ou un foulard de qualité pour ajouter une touche de style.")))

    @Rule(Cadeau(age="18-24ans", sexe="feminine", interest="voyage", occasion="anniversaire"))
    def fille_anniversaire_voyage(self):
        self.declare(Resultat(result=("Pour une jeune femme adulte aimant le voyage, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un sac à dos de voyage pratique et stylé \n"
                                        "- Une valise cabine légère et tendance \n"
                                        "- Un carnet de voyage pour documenter ses aventures \n"
                                        "- Une carte du monde à gratter pour marquer les endroits visités \n"
                                        "- Un adaptateur universel pour ses prises électriques à l’étranger \n"
                                        "- Une trousse de toilette de voyage élégante et fonctionnelle.")))

    @Rule(Cadeau(age="18-24ans", sexe="feminine", interest="technologie", occasion="anniversaire"))
    def fille_anniversaire_technologie(self):
        self.declare(Resultat(result=("Pour une jeune femme adulte aimant la technologie, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un casque ou des écouteurs Bluetooth de haute qualité \n"
                                        "- Un ordinateur portable ou une tablette élégante et performante \n"
                                        "- Un smartphone dernière génération ou un accessoire tendance (coque, chargeur sans fil) \n"
                                        "- Une montre connectée ou un bracelet fitness pour suivre son activité \n"
                                        "- Un abonnement à un service de streaming (musique, films, séries) \n"
                                        "- Un chargeur solaire portable ou une batterie externe pour recharger ses appareils partout.")))

    @Rule(Cadeau(age="18-24ans", sexe="feminine", interest="livres", occasion="anniversaire"))
    def fille_anniversaire_livres(self):
        self.declare(Resultat(result=("Pour une jeune femme adulte aimant les livres, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un roman à succès d’un auteur contemporain (ex. un thriller, un roman d’amour ou de science-fiction) \n"
                                        "- Un livre de développement personnel ou de bien-être \n"
                                        "- Un Kindle ou une liseuse électronique pour lire partout et tout le temps \n"
                                        "- Un abonnement à une box littéraire mensuelle pour découvrir de nouveaux livres chaque mois \n"
                                        "- Un livre de poésie contemporaine ou de classiques de la littérature")))

    @Rule(Cadeau(age="18-24ans", sexe="feminine", interest="sport", occasion="anniversaire"))
    def fille_anniversaire_sport(self):
        self.declare(Resultat(result=("Pour une jeune femme adulte aimant le sport, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un abonnement à une salle de sport ou à des cours de fitness en ligne \n"
                                        "- Une tenue de sport de marque avec des accessoires (legging, brassière, sweat) \n"
                                        "- Une montre connectée pour suivre ses performances sportives et sa santé \n"
                                        "- Un sac de sport tendance et pratique pour transporter son matériel \n"
                                        "- Un support pour smartphone afin de suivre des vidéos de sport pendant l’entraînement \n"
                                        "- Une corde à sauter de qualité professionnelle pour les entraînements à domicile \n"
                                        "- Une bouteille d’eau isotherme pour rester hydratée pendant les entraînements.")))

    @Rule(Cadeau(age="18-24ans", sexe="feminine", interest="jeux_vidéo", occasion="anniversaire"))
    def fille_anniversaire_jeux_video(self):
        self.declare(Resultat(result=("Pour une jeune femme adulte aimant les jeux video, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Une console de jeu dernière génération (PS5, Xbox Series X, Nintendo Switch) \n"
                                        "- Un abonnement à un service de jeux en ligne comme Xbox Game Pass ou Nintendo Switch Online \n"
                                        "- Des accessoires pour gamer comme une souris, un clavier mécanique, ou un casque gaming avec micro \n"
                                        "- Une chaise ergonomique pour gamer, confortable et adaptée pour de longues sessions \n"
                                        "- Une carte-cadeau pour sa plateforme de jeux préférée (Steam, PlayStation Store, Xbox Store) \n"
                                        "- Un jeu vidéo récent dans un genre qu'elle aime (RPG, aventure, stratégie, etc.) \n"
                                        "- Un support de casque ou un étui personnalisé pour ses jeux et accessoires.")))

    #fille------------------------------------------------------------------------------------------------------------------
    #graduation
    @Rule(Cadeau(age="18-24ans", sexe="feminine", interest="mode", occasion="graduation"))
    def fille_graduation_mode(self):
        self.declare(Resultat(result=("Pour une jeune femme adulte aimant la mode, voici des idées de cadeaux pour sa graduation : \n"
                                        "- Un vêtement iconique comme une robe de soirée ou une veste en cuir \n"
                                        "- Un parfum de marque avec une senteur moderne \n"
                                        "- Une montre \n"
                                        "- Un bon pour une séance de shopping avec un styliste personnel \n"
                                        "- Un ensemble de produits de beauté ou de maquillage haut de gamme \n"
                                        "- Une carte cadeau dans une boutique de mode \n"
                                        "- Un bijou (bracelet, collier, boucles d'oreilles) \n"
                                        "- Une écharpe ou un foulard de qualité pour ajouter une touche de style.")))
    
    @Rule(Cadeau(age="18-24ans", sexe="feminine", interest="voyage", occasion="graduation"))
    def fille_graduation_graduation(self):
        self.declare(Resultat(result=("Pour une jeune femme adulte aimant le voyage, voici des idées de cadeaux pour sa graduation : \n"
                                        "- Un guide de voyage ou un livre inspirant sur des destinations exotiques \n"
                                        "- Un appareil photo instantané pour capturer ses moments de voyage \n"
                                        "- Un sac à dos de voyage pratique et stylé \n"
                                        "- Une valise cabine légère et tendance \n"
                                        "- Une batterie portable pour recharger ses appareils en déplacement \n"
                                        "- Un kit de voyage incluant un oreiller de voyage, un masque de nuit et des bouchons d'oreilles \n")))

    @Rule(Cadeau(age="18-24ans", sexe="feminine", interest="technologie", occasion="graduation"))
    def fille_graduation_technologie(self):
        self.declare(Resultat(result=("Pour une jeune femme adulte aimant la technologie, voici des idées de cadeaux pour sa graduation : \n"
                                        "- Un appareil photo numérique ou un appareil instantané pour capturer des moments spéciaux \n"
                                        "- Un clavier mécanique ou une souris gaming ergonomique \n"
                                        "- Un smartphone dernière génération ou un accessoire tendance (coque, chargeur sans fil) \n"
                                        "- Une montre connectée ou un bracelet fitness pour suivre son activité \n"
                                        "- Un projecteur portable pour des soirées cinéma à la maison \n"
                                        "- Un chargeur sans fil design pour son bureau ou sa chambre ")))

    @Rule(Cadeau(age="18-24ans", sexe="feminine", interest="livres", occasion="graduation"))
    def fille_graduation_livres(self):
        self.declare(Resultat(result=("Pour une jeune femme adulte aimant les livres, voici des idées de cadeaux pour sa graduation : \n"
                                        "- Une édition collector d'un de ses livres favoris \n"
                                        "- Un livre de développement personnel ou de bien-être \n"
                                        "- Un Kindle ou une liseuse électronique pour lire partout et tout le temps \n"
                                        "- Une biographie d’une personnalité inspirante ou d’un leader dans son domaine \n"
                                        "- Un livre de fiction historique ou un roman inspiré de faits réels.")))

    @Rule(Cadeau(age="18-24ans", sexe="feminine", interest="sport", occasion="graduation"))
    def fille_graduation_sport(self):
        self.declare(Resultat(result=("Pour une jeune femme adulte aimant le sport, voici des idées de cadeaux pour sa graduation : \n"
                                        "- Un sac de gym personnalisé avec ses initiales \n"
                                        "- Une tenue de sport de marque avec des accessoires (legging, brassière, sweat) \n"
                                        "- Une montre connectée pour suivre ses performances sportives et sa santé \n"
                                        "- Un tapis de yoga haut de gamme avec des accessoires (blocs, sangle, coussin) \n"
                                        "- Un sac de sport tendance et pratique pour transporter son matériel \n"
                                        "- Un support pour smartphone afin de suivre des vidéos de sport pendant l’entraînement \n"
                                        "- Une paire de baskets de sport adaptées à son activité préférée (running, tennis, danse, etc.) \n"
                                        "- Une bouteille d’eau isotherme pour rester hydratée pendant les entraînements.")))

    @Rule(Cadeau(age="18-24ans", sexe="feminine", interest="jeux_vidéo", occasion="graduation"))
    def fille_graduation_jeux_video(self):
        self.declare(Resultat(result=("Pour une jeune femme adulte aimant les jeux video, voici des idées de cadeaux pour sa graduation : \n"
                                        "- Une lampe LED ou un éclairage d'ambiance pour personnaliser son espace de jeu \n"
                                        "- Une console de jeu dernière génération (PS5, Xbox Series X, Nintendo Switch) \n"
                                        "- Un abonnement à un service de jeux en ligne comme Xbox Game Pass ou Nintendo Switch Online \n"
                                        "- Des accessoires pour gamer comme une souris, un clavier mécanique, ou un casque gaming avec micro \n"
                                        "- Une chaise ergonomique pour gamer, confortable et adaptée pour de longues sessions \n"
                                        "- Une carte-cadeau pour des skins ou des objets dans son jeu vidéo préféré \n"
                                        "- Des posters, des figurines ou des objets de collection liés à ses jeux ou franchises préférées \n"
                                        "- Un support de console ou un système de rangement pour ses jeux et accessoires.")))
    
    #garcon------------------------------------------------------------------------------------------------------------------
    #anniversaire
    @Rule(Cadeau(age="18-24ans", sexe="masculin", interest="mode", occasion="anniversaire"))
    def garcon_anniversaire_mode(self):
        self.declare(Resultat(result=("Pour un jeune homme adulte aimant la mode, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Une montre ou bracelet \n"
                                        "- Une paire de baskets design de marques populaires (Nike, Adidas, etc.) \n"
                                        "- Un manteau ou une veste en cuir de qualité \n"
                                        "- Une carte cadeau dans une boutique de mode \n"
                                        "- Un ensemble de vêtements streetwear (hoodie, t-shirt graphique, pantalon cargo) \n"
                                        "- Un parfum de marque avec une senteur moderne \n"
                                        "- Une paire de lunettes de soleil stylées")))

    @Rule(Cadeau(age="18-24ans", sexe="masculin", interest="voyage", occasion="anniversaire"))
    def garcon_anniversaire_voyage(self):
        self.declare(Resultat(result=("Pour un jeune homme adulte aimant le voyage, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un sac à dos de voyage ultra-pratique et résistant \n"
                                        "- Une valise cabine légère et robuste \n"
                                        "- Un carnet de voyage pour documenter ses aventures \n"
                                        "- Une carte du monde à gratter pour marquer les endroits visités \n"
                                        "- Un adaptateur universel pour ses prises électriques à l’étranger \n"
                                        "- Un appareil photo ou une caméra d'action pour immortaliser ses aventures \n"
                                        "- Une trousse de toilette de voyage élégante et fonctionnelle. \n"
                                        "- Une application de voyage premium ou un abonnement à une plateforme de guide touristique \n")))

    @Rule(Cadeau(age="18-24ans", sexe="masculin", interest="technologie", occasion="anniversaire"))
    def garcon_anniversaire_technologie(self):
        self.declare(Resultat(result=("Pour un jeune homme adulte aimant la technologie, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un haut-parleur Bluetooth portable \n"
                                        "- Un écran portable ou un projecteur mini pour les présentations ou les projections de films \n"
                                        "- Un casque ou des écouteurs Bluetooth de haute qualité \n"
                                        "- Un ordinateur portable ou une tablette élégante et performante \n"
                                        "- Un smartphone dernière génération ou un accessoire tendance (coque, chargeur sans fil) \n"
                                        "- Une montre connectée ou un bracelet fitness pour suivre son activité \n"
                                        "- Un abonnement à un service de streaming (musique, films, séries) \n"
                                        "- Un ensemble de câbles et d'accessoires tech pratiques (adaptateurs, câbles USB, etc.) \n"
                                        "- Un assistant vocal intelligent (comme Amazon Echo ou Google Nest) \n")))

    @Rule(Cadeau(age="18-24ans", sexe="masculin", interest="livres", occasion="anniversaire"))
    def garcon_anniversaire_livres(self):
        self.declare(Resultat(result=("Pour un jeune homme adulte aimant les livres, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un abonnement à un service de livres audio (Audible, par exemple) \n"
                                        "- Un livre de développement personnel ou de bien-être \n"
                                        "- Une édition spéciale ou collector d’un de ses livres préférés \n"
                                        "- Un Kindle ou une liseuse électronique pour lire partout et tout le temps \n"
                                        "- Un abonnement à une box littéraire mensuelle pour découvrir de nouveaux livres chaque mois \n"
                                        "- Un livre sur la philosophie, la psychologie ou les sciences sociales pour élargir ses horizons")))

    @Rule(Cadeau(age="18-24ans", sexe="masculin", interest="sport", occasion="anniversaire"))
    def garcon_anniversaire_sport(self):
        self.declare(Resultat(result=("Pour un jeune homme adulte aimant le sport, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un abonnement à une salle de sport ou à un club sportif \n"
                                        "- Un équipement sportif de qualité (gant de boxe, chaussures de course, etc.) \n"
                                        "- Une tenue de sport de marque \n"
                                        "- Une montre connectée pour suivre ses performances sportives et sa santé \n"
                                        "- Un sac de sport pratique et élégant pour transporter son équipement \n"
                                        "- Un support pour smartphone afin de suivre des vidéos de sport pendant l’entraînement \n"
                                        "- Une corde à sauter de qualité professionnelle pour les entraînements à domicile \n"
                                        "- Un billet pour un match de sport ou un événement sportif majeur de son choix")))

    @Rule(Cadeau(age="18-24ans", sexe="masculin", interest="jeux_vidéo", occasion="anniversaire"))
    def garcon_anniversaire_jeux_video(self):
        self.declare(Resultat(result=("Pour un jeune homme adulte aimant les jeux video, voici des idées de cadeaux pour son anniversaire : \n"
                                        "- Un kit de personnalisation pour sa console (skins, autocollants, étuis, etc.) \n"
                                        "- Une console de jeu dernière génération (PS5, Xbox Series X, Nintendo Switch) \n"
                                        "- Un abonnement à un service de jeux en ligne comme Xbox Game Pass ou Nintendo Switch Online \n"
                                        "- Un casque gaming de haute qualité pour une meilleure immersion et communication \n"
                                        "- Une chaise ergonomique pour gamer, confortable et adaptée pour de longues sessions \n"
                                        "- Une carte-cadeau pour sa plateforme de jeux préférée (Steam, PlayStation Store, Xbox Store) \n"
                                        "- Un jeu vidéo récent dans un genre qu'elle aime (RPG, aventure, stratégie, etc.) \n"
                                        "- Un support de casque ou un étui personnalisé pour ses jeux et accessoires.\n"
                                        "- Un nouveau jeu vidéo pour sa console préférée (PlayStation, Xbox, Nintendo Switch, etc.) \n")))

    #garcon------------------------------------------------------------------------------------------------------------------
    #graduation
    @Rule(Cadeau(age="18-24ans", sexe="masculin", interest="mode", occasion="graduation"))
    def garcon_graduation_mode(self):
        self.declare(Resultat(result=("Pour un jeune homme adulte aimant la mode, voici des idées de cadeaux pour sa graduation : \n"
                                        "- Un portefeuille ou une ceinture en cuir de marque \n"
                                        "- Une montre ou bracelet \n"
                                        "- Une paire de baskets design de marques populaires (Nike, Adidas, etc.) \n"
                                        "- Un manteau ou une veste en cuir de qualité \n"
                                        "- Une chemise ou un polo bien coupé, avec une coupe moderne \n"
                                        "- Un sac à dos ou une sacoche en cuir ou en toile pour un look urbain \n"
                                        "- Un parfum de marque avec une senteur moderne \n"
                                        "- Une paire de lunettes de soleil stylées")))
    
    @Rule(Cadeau(age="18-24ans", sexe="masculin", interest="voyage", occasion="graduation"))
    def garcon_graduation_voyage(self):
        self.declare(Resultat(result=("Pour un jeune homme adulte aimant le voyage, voici des idées de cadeaux pour sa graduation : \n"
                                        "- Une tente ou un équipement de camping pour les amateurs de nature \n"
                                        "- Un sac à dos de voyage ultra-pratique et résistant \n"
                                        "- Une valise cabine légère et robuste \n"
                                        "- Une montre GPS ou une montre étanche pour les activités en extérieur \n"
                                        "- Une carte du monde à gratter pour marquer les endroits visités \n"
                                        "- Un adaptateur universel pour ses prises électriques à l’étranger \n"
                                        "- Un appareil photo ou une caméra d'action pour immortaliser ses aventures \n"
                                        "- Une trousse de toilette de voyage élégante et fonctionnelle. \n"
                                        "- Des vêtements de voyage pratiques et confortables (vestes, t-shirts techniques, pantalons résistants, etc.)")))

    @Rule(Cadeau(age="18-24ans", sexe="masculin", interest="technologie", occasion="graduation"))
    def garcon_graduation_technologie(self):
        self.declare(Resultat(result=("Pour un jeune homme adulte aimant la technologie, voici des idées de cadeaux pour sa graduation : \n"
                                        "- Un clavier mécanique ou une souris gaming ergonomique \n"
                                        "- Un écran portable ou un projecteur mini pour les présentations ou les projections de films \n"
                                        "- Un appareil photo numérique ou un appareil instantané pour capturer des moments spéciaux \n"
                                        "- Un casque ou des écouteurs Bluetooth de haute qualité \n"
                                        "- Une montre connectée ou un bracelet fitness \n"
                                        "- Un smartphone dernière génération ou un accessoire tendance (coque, chargeur sans fil) \n"
                                        "- Une montre connectée ou un bracelet fitness pour suivre son activité \n"
                                        "- Un smartphone dernière génération ou un accessoire tendance (coque, chargeur sans fil).")))

    @Rule(Cadeau(age="18-24ans", sexe="masculin", interest="livres", occasion="graduation"))
    def garcon_graduation_livres(self):
        self.declare(Resultat(result=("Pour un jeune homme adulte aimant les livres, voici des idées de cadeaux pour sa graduation : \n"
                                        "- Un abonnement à un service de livres audio (Audible, par exemple) \n"
                                        "- Un livre de développement personnel ou de bien-être \n"
                                        "- Une édition spéciale ou collector d’un de ses livres préférés \n"
                                        "- Un Kindle ou une liseuse électronique pour lire partout et tout le temps \n"
                                        "- Une biographie d’une personnalité inspirante ou d’un leader dans son domaine \n"
                                        "- Un carnet de notes de qualité pour écrire ses propres idées ou ses récits \n"
                                        "- Un livre de fiction historique ou un roman inspiré de faits réels.")))

    @Rule(Cadeau(age="18-24ans", sexe="masculin", interest="sport", occasion="graduation"))
    def garcon_graduation_sport(self):
        self.declare(Resultat(result=("Pour un jeune homme adulte aimant le sport, voici des idées de cadeaux pour sa graduation : \n"
                                        "- Un coach personnel ou une application de sport pour améliorer ses performances \n"
                                        "- Un sac de gym personnalisé avec ses initiales \n"
                                        "- Une tenue de sport de marque \n"
                                        "- Une montre connectée pour suivre ses performances sportives et sa santé \n"
                                        "- Un sac de sport tendance et pratique pour transporter son matériel \n"
                                        "- Un support pour smartphone afin de suivre des vidéos de sport pendant l’entraînement \n"
                                        "- Une paire de baskets de sport adaptées à son activité préférée (running, tennis, danse, etc.) \n"
                                        "- Un massage sportif ou une séance de kinésithérapie pour récupérer après un entraînement intense")))

    @Rule(Cadeau(age="18-24ans", sexe="masculin", interest="jeux_vidéo", occasion="graduation"))
    def garcon_graduation_jeux_video(self):
        self.declare(Resultat(result=("Pour un jeune homme adulte aimant les jeux video, voici des idées de cadeaux pour sa graduation : \n"
                                        "- Une manette de jeu personnalisée ou un accessoire gaming (clavier mécanique, souris de gaming, etc.) \n"
                                        "- Une lampe LED ou un éclairage d'ambiance pour personnaliser son espace de jeu \n"
                                        "- Une console de jeu dernière génération (PS5, Xbox Series X, Nintendo Switch) \n"
                                        "- Un abonnement à un service de jeux en ligne comme Xbox Game Pass ou Nintendo Switch Online \n"
                                        "- Des accessoires pour gamer comme une souris, un clavier mécanique, ou un casque gaming avec micro \n"
                                        "- Une chaise ergonomique pour gamer, confortable et adaptée pour de longues sessions \n"
                                        "- Une carte-cadeau pour des skins ou des objets dans son jeu vidéo préféré \n"
                                        "- Des posters, des figurines ou des objets de collection liés à ses jeux ou franchises préférées \n"
                                        "- Un support de console ou un système de rangement pour ses jeux et accessoires.")))
