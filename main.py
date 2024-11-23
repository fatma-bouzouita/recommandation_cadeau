from flask import Flask, render_template, request
from experta import *

app = Flask(__name__)

# Définition du fait Cadeau
class Cadeau(Fact):
    """Fait représentant un cadeau basé sur l'âge, sexe, et centre d'intérêt."""
    pass

# Définir un fait pour les résultats
class Resultat(Fact):
    """Fait pour stocker les résultats des recommandations."""
    pass

# Définir les règles de recommandation
class InterfaceEngine(KnowledgeEngine):
    
    #0-2 ans garçon
    @Rule(Cadeau(age="0-2ans"), Cadeau(sexe="masculin"), Cadeau(occasion="naissance"))
    def cadeau_naissance_garcon(self):
        self.declare(Resultat(result=(
            "Pour une naissance (garçon), voici des idées de cadeaux : \n"
            "- Ensemble de vêtements pour nouveau-né (ex : grenouillère à motifs) \n"
            "- Jouet d'éveil interactif (ex : hochets en forme de voitures ou animaux) \n"
            "- Mobile avec des couleurs et formes vives pour le berceau \n"
            "- Coffret souvenir personnalisé (ex : boîte à souvenirs, bracelet gravé) \n"
            "- Couverture douce et confortable aux motifs animaliers."
        )))

    @Rule(Cadeau(age="0-2ans"), Cadeau(sexe="masculin"), Cadeau(occasion="anniversaire"))
    def cadeau_anniversaire_garcon(self):
        self.declare(Resultat(result=(
            "Pour un anniversaire (garçon), voici des idées : \n"
            "- Voiture ou train en bois adaptés aux tout-petits \n"
            "- Puzzle ou jeux de construction simples \n"
            "- Tapis d'éveil ou de jeu interactif \n"
            "- Livre avec des personnages ou animaux à toucher \n"
            "- Peluches thématiques (ex : dinosaure, super-héros) \n"
            "- Veilleuse colorée en forme de fusée ou étoile."
            "- Ensemble de vêtements thématiques (ex : super-héros ou animaux)."
        )))

    # kif nzidhom ywali yaady hethom baed saat o inegligi occasion
        
    # @Rule(Cadeau(age="0-2ans"), Cadeau(sexe="masculin"))
    # def cadeau_bebe_garcon(self):
    #     self.declare(Resultat(result=(
    #         "Pour un garçon de 0-2 ans, vous pouvez offrir : \n"
    #         "- Jouets d'éveil adaptés à son âge (ex : cubes empilables, puzzles simples) \n"
    #         "- Livres interactifs ou sonores \n"
    #         "- Tapis de jeu coloré \n"
    #         "- Peluches ou jouets thématiques (voitures, animaux)."
    #         "- Ensemble de vêtements adaptés à la saison \n"
    #         "- Veilleuses avec musique apaisante \n"
    #         )))

    # 0-2 ans fille
    @Rule(Cadeau(age="0-2ans"), Cadeau(sexe="feminine"), Cadeau(occasion="naissance"))
    def cadeau_naissance_fille(self):
        self.declare(Resultat(result=(
        "Pour une naissance (fille), voici des idées de cadeaux : \n"
        "- Robe ou ensemble de vêtements avec des motifs doux (ex : fleurs, étoiles) \n"
        "- Poupée ou peluche en tissu hypoallergénique \n"
        "- Bracelet de naissance ou boîte à bijoux personnalisée \n"
        "- Mobile musical en couleurs pastel pour le berceau \n"
        "- Couverture douce personnalisée avec le prénom."
        )))

    @Rule(Cadeau(age="0-2ans"), Cadeau(sexe="feminine"), Cadeau(occasion="anniversaire"))
    def cadeau_anniversaire_fille(self):
            self.declare(Resultat(result=(
            "Pour un anniversaire (fille), voici des idées : \n"
            "- Poupées interactives ou peluches thématiques (ex : licornes, princesses) \n"
            "- Livres d'éveil colorés avec textures (ex : livres en tissu ou en plastique) \n"
            "- Tapis d'éveil musical ou en forme de fleurs \n"
            "- Jouets d'éveil éducatifs (ex : cubes avec formes géométriques) \n"
            "- Ensemble d'accessoires mignons (ex : bandeaux, chaussettes colorées)."
            "- Tapis de jeu décoratif ou musical \n"
            )))

    # @Rule(Cadeau(age="0-2ans"), Cadeau(sexe="feminine"))
    # def cadeau_bebe_fille(self):
    #     self.declare(Resultat(result=(
    #         "Pour une fille de 0-2 ans, vous pouvez offrir : \n"
    #         "- Jouets interactifs avec textures et couleurs vives \n"
    #         "- Peluches ou poupées adaptées à son âge \n"
    #         "- Robes ou ensembles de vêtements doux \n"
    #         "- Jouets sensoriels d'éveil (ex : jouets en silicone, anneaux de dentition) \n"
    #         "- Couverture douce personnalisée \n"
    #         "- Livres avec textures et illustrations colorées \n"
    #         "- Veilleuses en forme d'animaux ou avec lumière douce."
    #         )))

    # Petite enfance : 3-5 ans
    @Rule(Cadeau(age="3-5ans"), Cadeau(interest="dessin"))
    def cadeau_enfant_dessin(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Livres à colorier \n"
                                       "- Feutres lavables \n"
                                       "- Kit de dessin pour enfants")))

    @Rule(Cadeau(age="3-5ans"), Cadeau(interest="histoires"))
    def cadeau_enfant_histoires(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Livres illustrés \n"
                                       "- Marionnettes \n"
                                       "- Coffret d'histoires audio")))

    # Enfance moyenne : 6-9 ans
    @Rule(Cadeau(age="6-9ans"), Cadeau(interest="jeux_de_construction"))
    def cadeau_enfant_construction(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Lego \n"
                                       "- Meccano \n"
                                       "- Puzzles 3D")))

    @Rule(Cadeau(age="6-9ans"), Cadeau(interest="sport"))
    def cadeau_enfant_sport(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Ballon de football \n"
                                       "- Trottinette \n"
                                       "- Mini-table de ping-pong")))

    # Adolescents : 10-17 ans
    @Rule(Cadeau(age="13-17ans"), Cadeau(interest="technologie"))
    def cadeau_adolescent_technologie(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Casque audio \n"
                                       "- Montre connectée \n"
                                       "- Mini-drone")))

    @Rule(Cadeau(age="13-17ans"), Cadeau(interest="jeux_video"))
    def cadeau_adolescent_jeux_video(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Carte cadeau Steam \n"
                                       "- Manette de jeu \n"
                                       "- Abonnement à un service de jeux en ligne")))

    # Adultes jeunes : 18-40 ans
    @Rule(Cadeau(age="18-24ans"), Cadeau(interest="voyage"))
    def cadeau_jeune_adulte_voyage(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Sac à dos de voyage \n"
                                       "- Carnet de voyage \n"
                                       "- Appareil photo instantané")))

    @Rule(Cadeau(age="25-40ans"), Cadeau(interest="cuisine"))
    def cadeau_adulte_cuisine(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Robot de cuisine \n"
                                       "- Cours de cuisine \n"
                                       "- Livre de recettes gastronomiques")))

    # Seniors : 60 ans et plus
    @Rule(Cadeau(age="60plus"), Cadeau(interest="jardinage"))
    def cadeau_senior_jardinage(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Outils de jardin ergonomiques \n"
                                       "- Livres sur les plantes \n"
                                       "- Abonnement à un magazine de jardinage")))

    @Rule(Cadeau(age="60plus"), Cadeau(interest="confort"))
    def cadeau_senior_confort(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Coussin chauffant \n"
                                       "- Plaid doux \n"
                                       "- Pantoufles confortables")))



# Initialiser le moteur d'inférence
engine = InterfaceEngine()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Récupérer les informations soumises par l'utilisateur
        age = request.form["age"]
        sexe = request.form["sexe"]
        interest = request.form["interest"]
        occasion = request.form["occasion"]
        print(age,sexe,occasion)

        # Créer l'instance du moteur de règles
        engine = InterfaceEngine()

        # Déclarer le fait avec les données soumises par l'utilisateur
        engine.declare(Cadeau(age=age, sexe=sexe, interest=interest,occasion=occasion))

        # Exécuter le moteur de règles pour obtenir le résultat
        engine.run()
        
        # Obtenir le résultat des recommandations
        result = None
        for fact in engine.facts.values():
            if isinstance(fact, Resultat):
                result = fact["result"]

        return render_template("index.html", result=result)
    
    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)