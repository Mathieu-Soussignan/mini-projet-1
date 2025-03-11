import json
from fastapi import FastAPI
# Inclusion de vos routes existantes (sans modification)
from routes import (
    patient_routes,
    sex_routes,
    region_routes,
    smoker_routes,
    app_user_routes
)
from sqlalchemy.orm import DeclarativeMeta
from modules.database import init_db

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        # Si l'objet est une instance d'un modèle SQLAlchemy, on le convertit en dict
        if isinstance(obj.__class__, DeclarativeMeta):
            # On exclut les attributs internes (_sa_instance_state, etc.)
            fields = {}
            for field in obj.__table__.columns.keys():
                fields[field] = getattr(obj, field)
            return fields
        return super().default(obj)


app = FastAPI()

# Définir l'encodeur JSON personnalisé pour l'application
app.json_encoder = AlchemyEncoder

# Création des tables dans la base de données au démarrage
init_db()

app.include_router(sex_routes.router, prefix="/sex", tags=["Sex"])
app.include_router(region_routes.router, prefix="/regions", tags=["Regions"])
app.include_router(smoker_routes.router, prefix="/smoker", tags=["Smoker"])
app.include_router(patient_routes.router, prefix="/utilisateurs", tags=["Utilisateurs"]) # noqa
app.include_router(app_user_routes.router, prefix="/app_user", tags=["AppUser"]) # noqa