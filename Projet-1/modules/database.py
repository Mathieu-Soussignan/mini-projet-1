from models.base import Base, engine, SessionLocal

# Importer tous les modèles pour qu'ils soient enregistrés dans le metadata
from models.sex_model import Sex            # noqa: F401
from models.region_model import Region      # noqa: F401
from models.smoker_model import Smoker      # noqa: F401
from models.app_user_model import AppUser   # noqa: F401
from models.patient_model import Patient    # noqa: F401


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
