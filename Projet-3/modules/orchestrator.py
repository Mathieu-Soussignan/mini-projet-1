import requests
from modules.logger import logger


def get_utilisateurs(api_proj1_url: str = "http://api-proj1:8000"):
    """
    Récupère la liste des patients depuis l'API du Projet 1.
    Par défaut, utilise l'URL "http://api-proj1:8000" (service défini dans docker-compose). # noqa
    """
    endpoint = f"{api_proj1_url}/utilisateurs/"
    try:
        response = requests.get(endpoint, timeout=5)
        response.raise_for_status()
        logger.info("GET utilisateurs successful")
        return response.json()
    except Exception as e:
        logger.error(f"Error getting utilisateurs: {e}")
        return None


def predict_charges(api_proj2_url: str = "http://api-proj2:8000", # noqa
                    age: float = None, bmi: float = None, children: int = None,
                    sex: str = None, smoker: str = None, region: str = None):
    """
    Envoie une requête de prédiction de charges à l'API du Projet 2.
    Par défaut, utilise l'URL "http://api-proj2:8000" (service défini dans docker-compose). # noqa
    """
    endpoint = f"{api_proj2_url}/predict"
    payload = {
        "age": age,
        "bmi": bmi,
        "children": children,
        "sex": sex,
        "smoker": smoker,
        "region": region
    }
    try:
        response = requests.post(endpoint, json=payload, timeout=5)
        response.raise_for_status()
        logger.info("POST predict successful")
        data = response.json()
        return data.get("predicted_charges")
    except Exception as e:
        logger.error(f"Error predicting charges: {e}")
        return None # noqa