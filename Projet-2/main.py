from fastapi import FastAPI
from pydantic import BaseModel
import joblib
# import numpy as np
import uvicorn

app = FastAPI(title="Projet 2 – API de Prédiction des Charges Médicales")

# Charger le modèle sauvegardé (assurez-vous que ce modèle inclut le préprocesseur)  # noqa: E501
model = joblib.load("./scripts/best_model.pkl")


# Modèle d'entrée pour la prédiction
class PredictionInput(BaseModel):
    # Ces champs correspondent aux données brutes telles qu'elles étaient dans le CSV  # noqa: E501
    age: float
    bmi: float
    children: int
    sex: str
    smoker: str
    region: str


@app.post("/predict")
def predict(input: PredictionInput):
    """
    Prédit les charges médicales à partir des features fournies.
    Pour cet exemple, nous supposons que le modèle sauvegardé est un pipeline complet.  # noqa: E501
    """
    # Convertir l'input en dict pour extraire les valeurs dans le bon ordre.
    # Si le pipeline sauvegardé inclut le préprocesseur, il suffira de transmettre un DataFrame.  # noqa: E501
    input_data = {
        "age": [input.age],
        "bmi": [input.bmi],
        "children": [input.children],
        "sex": [input.sex],
        "smoker": [input.smoker],
        "region": [input.region]
    }

    # Pour simplifier, on utilise un DataFrame, en supposant que le pipeline sauvegardé peut traiter ce format. # noqa: E501
    import pandas as pd
    df_input = pd.DataFrame(input_data)

    prediction = model.predict(df_input)
    return {"predicted_charges": float(prediction[0])}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)  # noqa: W292, E501