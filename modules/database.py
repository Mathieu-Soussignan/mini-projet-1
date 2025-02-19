from models.base import Base, engine, SessionLocal

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