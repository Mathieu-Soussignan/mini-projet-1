from models.base import Base, engine, SessionLocal

# Importer tous les modèles pour qu'ils soient enregistrés dans le metadata
from models.sex_model import Sex
from models.region_model import Region
from models.smoker_model import Smoker
from models.app_user_model import AppUser
from models.patient_model import Patient

def init_db():
    """Crée les tables dans la base de données."""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Fournit une session de base de données pour une requête FastAPI."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()