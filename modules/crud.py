from sqlalchemy.orm import Session

from models.sex_model import Sex
from models.region_model import Region
from models.smoker_model import Smoker
from models.app_user_model import AppUser
from models.patient_model import Patient

# ----------------------
# CRUD pour Sex
# ----------------------
def create_sex(db: Session, sex_label: str):
    new_sex = Sex(sex_label=sex_label)
    db.add(new_sex)
    db.commit()
    db.refresh(new_sex)
    return new_sex

def get_sex(db: Session, sex_id: int):
    return db.query(Sex).filter(Sex.id_sex == sex_id).first()

def get_sexes(db: Session):
    return db.query(Sex).all()

def update_sex(db: Session, sex_id: int, sex_label: str):
    sex = get_sex(db, sex_id)
    if not sex:
        return None
    sex.sex_label = sex_label
    db.commit()
    db.refresh(sex)
    return sex

def delete_sex(db: Session, sex_id: int):
    sex = get_sex(db, sex_id)
    if sex:
        db.delete(sex)
        db.commit()
        return True
    return False


# ----------------------
# CRUD pour Region
# ----------------------
def create_region(db: Session, region_name: str):
    new_region = Region(region_name=region_name)
    db.add(new_region)
    db.commit()
    db.refresh(new_region)
    return new_region

def get_region(db: Session, region_id: int):
    return db.query(Region).filter(Region.id_region == region_id).first()

def get_regions(db: Session):
    return db.query(Region).all()

def update_region(db: Session, region_id: int, region_name: str):
    region = get_region(db, region_id)
    if not region:
        return None
    region.region_name = region_name
    db.commit()
    db.refresh(region)
    return region

def delete_region(db: Session, region_id: int):
    region = get_region(db, region_id)
    if region:
        db.delete(region)
        db.commit()
        return True
    return False


# ----------------------
# CRUD pour Smoker
# ----------------------
def create_smoker(db: Session, is_smoker: str):
    """
    is_smoker peut être "yes", "no", ou tout autre label.
    """
    new_smoker = Smoker(is_smoker=is_smoker)
    db.add(new_smoker)
    db.commit()
    db.refresh(new_smoker)
    return new_smoker

def get_smoker(db: Session, smoker_id: int):
    return db.query(Smoker).filter(Smoker.id_smoker == smoker_id).first()

def get_smokers(db: Session):
    return db.query(Smoker).all()

def update_smoker(db: Session, smoker_id: int, is_smoker: str):
    smoker = get_smoker(db, smoker_id)
    if not smoker:
        return None
    smoker.is_smoker = is_smoker
    db.commit()
    db.refresh(smoker)
    return smoker

def delete_smoker(db: Session, smoker_id: int):
    smoker = get_smoker(db, smoker_id)
    if smoker:
        db.delete(smoker)
        db.commit()
        return True
    return False


# ----------------------
# CRUD pour AppUser
# ----------------------
def create_app_user(db: Session, username: str, password: str, user_email: str):
    new_user = AppUser(username=username, password=password, user_email=user_email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_app_user(db: Session, user_id: int):
    return db.query(AppUser).filter(AppUser.id_user == user_id).first()

def get_app_users(db: Session):
    return db.query(AppUser).all()

def update_app_user(db: Session, user_id: int, **kwargs):
    user = get_app_user(db, user_id)
    if not user:
        return None
    for key, value in kwargs.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return user

def delete_app_user(db: Session, user_id: int):
    user = get_app_user(db, user_id)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False


# ----------------------
# CRUD pour Patient
# ----------------------
def create_patient(
    db: Session,
    last_name: str,
    first_name: str,
    age: int = None,
    bmi: float = None,
    patient_email: str = None,
    children: int = None,
    charges: float = None,
    sex_id: int = None,
    region_id: int = None,
    smoker_id: int = None,
    user_id: int = None
):
    new_patient = Patient(
        last_name=last_name,
        first_name=first_name,
        age=age,
        bmi=bmi,
        patient_email=patient_email,
        children=children,
        charges=charges,
        sex_id=sex_id,
        region_id=region_id,
        smoker_id=smoker_id,
        user_id=user_id
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

def get_patient(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id_patient == patient_id).first()

def get_patients(db: Session):
    return db.query(Patient).all()

def update_patient(db: Session, patient_id: int, **kwargs):
    patient = get_patient(db, patient_id)
    if not patient:
        return None
    for key, value in kwargs.items():
        setattr(patient, key, value)
    db.commit()
    db.refresh(patient)
    return patient

def delete_patient(db: Session, patient_id: int):
    patient = get_patient(db, patient_id)
    if patient:
        db.delete(patient)
        db.commit()
        return True
    return False