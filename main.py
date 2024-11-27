from flask import Flask, render_template, request
from experta import *
from models.facts import Cadeau, Resultat
from rules.r_0_2ans import  InterfaceEngine_0_2ans
from rules.r_12_17ans import InterfaceEngine_12_17ans 
from rules.r_18_24 import InterfaceEngine_18_24ans
from rules.r_25_40 import InterfaceEngine_25_40ans
from rules.r_3_5_ans import InterfaceEngine_3_5ans
from rules.r_41_60 import InterfaceEngine_41_60ans 
from rules.r_60 import InterfaceEngine_60ans
from rules.r_6_11ans import InterfaceEngine_6_11ans

app = Flask(__name__)

# Dictionnaire des moteurs par tranche d'âge
AGE_ENGINE_MAP = {
    "0-2ans":   InterfaceEngine_0_2ans,
    "3-5ans":   InterfaceEngine_3_5ans,
    "6-11ans":   InterfaceEngine_6_11ans,
    "12-17ans": InterfaceEngine_12_17ans,
    "18-24ans": InterfaceEngine_18_24ans,
    "25-40ans": InterfaceEngine_25_40ans,
    "41-60ans": InterfaceEngine_41_60ans,
    "60plus":   InterfaceEngine_60ans,

}   

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Récupérer les informations soumises par l'utilisateur
        age = request.form["age"]
        sexe = request.form["sexe"]
        interest = request.form["interest"]
        occasion = request.form["occasion"]
        print(age,sexe,occasion,interest)

        engine_class = AGE_ENGINE_MAP.get(age)
        if engine_class is None:
            return render_template("index.html", result="Aucun moteur de règles pour cette tranche d'âge.")
        
        #instance du moteur de règles pour l'âge sélectionné
        engine = engine_class()
        engine.reset()
        # Déclarer le fait avec les données soumises par l'utilisateur
        engine.declare(Cadeau(age=age, sexe=sexe, interest=interest, occasion=occasion))
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