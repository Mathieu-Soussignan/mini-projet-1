import pandas as pd
from faker import Faker
from sqlalchemy.orm import Session
from models.patient_model import Patient
from models.sex_model import Sex
from models.region_model import Region
from models.smoker_model import Smoker
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
        sex_obj = db.query(Sex).filter(Sex.sex_label == sex_value).first()
        if not sex_obj:
            sex_obj = Sex(sex_label=sex_value)
            db.add(sex_obj)
            db.commit()
            db.refresh(sex_obj)

        # 2. Gestion de la Région
        region_value = row['region']
        region_obj = db.query(Region).filter(Region.region_name == region_value).first() # noqa
        if not region_obj:
            region_obj = Region(region_name=region_value)
            db.add(region_obj)
            db.commit()
            db.refresh(region_obj)
        # 3. Gestion du statut fumeur (Smoker)
        smoker_value = row['smoker']
        smoker_obj = db.query(Smoker).filter(Smoker.is_smoker == smoker_value).first() # noqa
        if not smoker_obj:
            smoker_obj = Smoker(is_smoker=smoker_value)
            db.add(smoker_obj)
            db.commit()
            db.refresh(smoker_obj)

        # 4. Génération de nom et prénom via Faker
        first_name = fake.first_name()
        last_name = fake.last_name()
        # 5. Création d'un enregistrement Patient
        patient = Patient(
            last_name=last_name,
            first_name=first_name,
            age=row['age'],
            bmi=row['bmi'],
            children=row['children'],
            charges=row['charges'],
            # Optionnel : email du patient si disponible
            patient_email=None,
            sex_id=sex_obj.id_sex,
            region_id=region_obj.id_region,
            smoker_id=smoker_obj.id_smoker,
            user_id=None  # À renseigner si le patient a un compte utilisateur associé # noqa
        )
        db.add(patient)
        db.commit()
        db.refresh(patient)
    db.close()
    print("Import terminé.")


if __name__ == "__main__":
    import_insurance_csv("insurance.csv") # noqa