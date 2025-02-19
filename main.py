from fastapi import FastAPI
from routes import (
    sex_routes,
    region_routes,
    charge_routes,
    utilisateur_routes,
    transaction_routes
)
from modules.database import init_db

app = FastAPI()

# Création des tables dans la base de données au démarrage
init_db()

# Inclusion des routers pour chaque entité
app.include_router(sex_routes.router, prefix="/sex", tags=["Sex"])
app.include_router(region_routes.router, prefix="/regions", tags=["Regions"])
app.include_router(charge_routes.router, prefix="/charges", tags=["Charges"])
app.include_router(utilisateur_routes.router, prefix="/utilisateurs", tags=["Utilisateurs"])
app.include_router(transaction_routes.router, prefix="/transactions", tags=["Transactions"])