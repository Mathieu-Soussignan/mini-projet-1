import pandas as pd
from faker import Faker
from sqlalchemy.orm import Session
from models.utilisateur_model import Utilisateur
from models.transaction_model import Transaction
from models.charge_model import Charge
from models.sex_model import Sex
from models.region_model import Region
from modules.database import SessionLocal, init_db

fake = Faker('fr_FR')

def import_insurance_csv(csv_path: str):
    # Crée les tables si ce n'est pas déjà fait
    init_db()
    db: Session = SessionLocal()

    # Lire le CSV
    df = pd.read_csv(csv_path)

    for index, row in df.iterrows():
        # 1. Gestion du Sexe
        sex_value = row['sex']
        sex_obj = db.query(Sex).filter(Sex.type == sex_value).first()
        if not sex_obj:
            sex_obj = Sex(type=sex_value)
            db.add(sex_obj)
            db.commit()
            db.refresh(sex_obj)
        
        # 2. Gestion de la Région
        region_value = row['region']
        region_obj = db.query(Region).filter(Region.region_name == region_value).first()
        if not region_obj:
            region_obj = Region(region_name=region_value)
            db.add(region_obj)
            db.commit()
            db.refresh(region_obj)
        
        # 3. Génération de user_name via Faker
        first_name = fake.first_name()
        last_name = fake.last_name()
        user_name = f"{first_name} {last_name}"
        
        # 4. Création d'un enregistrement Utilisateur (Patient)
        utilisateur = Utilisateur(
            user_name=user_name,
            age=row['age'],
            bmi=row['bmi'],
            children=row['children'],
            smoker=row['smoker'],
            sex_id=sex_obj.sex_id,
            region_id=region_obj.region_id
        )
        db.add(utilisateur)
        db.commit()
        db.refresh(utilisateur)
        
        # 5. Création d'un enregistrement Charge
        charge = Charge(price=row['charges'])
        db.add(charge)
        db.commit()
        db.refresh(charge)
        
        # 6. Création d'une Transaction liant l'utilisateur à la charge
        transaction = Transaction(
            user_id=utilisateur.user_id,
            charge_id=charge.charge_id
        )
        db.add(transaction)
        db.commit()

    db.close()
    print("Import terminé.")


if __name__ == "__main__":
    import_insurance_csv("insurance.csv")