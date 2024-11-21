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

    @Rule(Cadeau(age="0-2ans"), Cadeau(sexe="masculin"))
    def cadeau_bebe_garcon(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Nounours \n"
                                       "- Ensemble de vêtements \n"
                                       "- Jouets sensoriels")))
        
    @Rule(Cadeau(age="0-2ans"), Cadeau(sexe="feminine"))
    def cadeau_bebe_fille(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Robe \n"
                                       "- Bracelet de naissance \n"
                                       "- Couverture rose")))

   

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
        
        # Créer l'instance du moteur de règles
        engine = InterfaceEngine()

        # Déclarer le fait avec les données soumises par l'utilisateur
        engine.declare(Cadeau(age=age, sexe=sexe, interest=interest))

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