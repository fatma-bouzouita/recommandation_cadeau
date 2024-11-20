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

    @Rule(Cadeau(age="entre0et3ans"), Cadeau(sexe="masculin"))
    def cadeau_bebe_garcon(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Nounours \n"
                                       "- Ensemble de vêtements \n"
                                       "- Jouets sensoriels")))
        
    @Rule(Cadeau(age="entre0et3ans"), Cadeau(sexe="feminine"))
    def cadeau_bebe_fille(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Robe \n"
                                       "- Bracelet de naissance \n"
                                       "- Couverture rose")))

    @Rule(Cadeau(age="entre4et9ans"), Cadeau(sexe="masculin"), Cadeau(interest="football"))
    def cadeau_enfant_garcon(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Un ballon \n"
                                       "- Une voiture commandée à distance \n"
                                       "- Un pull avec un dessin de chien")))

    # Exemple de règle pour une adolescente intéressée par le théâtre
    @Rule(Cadeau(age="entre10et16ans"), Cadeau(sexe="feminine"), Cadeau(interest="theatre"))
    def cadeau_adolescente_theatre(self):
        self.declare(Resultat(result=("Vous pouvez lui offrir: \n"
                                       "- Un ticket pour une pièce de théâtre \n"
                                       "- Une robe colorée \n"
                                       "- Une petite tortue")))

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