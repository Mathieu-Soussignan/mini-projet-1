from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Charger le modèle sauvegardé
model = joblib.load("best_model.pkl")


# Définir le modèle d'entrée (ajustez les champs en fonction du prétraitement)
class PredictionInput(BaseModel):
    age: float
    bmi: float
    children: int
    # Ajoutez d'autres features si nécessaire (par exemple, encodées via OneHot ou autres) # noqa: E501


@app.post("/predict")
def predict(input: PredictionInput):
    # Convertir l'input en tableau numpy
    features = np.array([[input.age, input.bmi, input.children]])
    # Vous devrez peut-être appliquer le même prétraitement que lors de l'entraînement  # noqa: E501
    prediction = model.predict(features)
    return {"predicted_charges": float(prediction[0])}  # noqa: E501, W292