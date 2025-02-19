from sqlalchemy.orm import Session
from models.sex_model import Sex
from models.region_model import Region
from models.utilisateur_model import Utilisateur
from models.charge_model import Charge
from models.transaction_model import Transaction

# ----------------------
# CRUD pour Sex
# ----------------------
def create_sex(db: Session, type: str):
    new_sex = Sex(type=type)
    db.add(new_sex)
    db.commit()
    db.refresh(new_sex)
    return new_sex

def get_sex(db: Session, sex_id: int):
    return db.query(Sex).filter(Sex.sex_id == sex_id).first()

def get_sexes(db: Session):
    return db.query(Sex).all()

def update_sex(db: Session, sex_id: int, type: str):
    sex = get_sex(db, sex_id)
    if not sex:
        return None
    sex.type = type
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
    return db.query(Region).filter(Region.region_id == region_id).first()

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
# CRUD pour Utilisateur
# ----------------------
def create_utilisateur(db: Session, user_name: str, age: int = None, bmi: float = None, children: int = None, smoker: str = None, sex_id: int = None, region_id: int = None):
    new_utilisateur = Utilisateur(
        user_name=user_name,
        age=age,
        bmi=bmi,
        children=children,
        smoker=smoker,
        sex_id=sex_id,
        region_id=region_id
    )
    db.add(new_utilisateur)
    db.commit()
    db.refresh(new_utilisateur)
    return new_utilisateur

def get_utilisateur(db: Session, user_id: int):
    return db.query(Utilisateur).filter(Utilisateur.user_id == user_id).first()

def get_utilisateurs(db: Session):
    return db.query(Utilisateur).all()

def update_utilisateur(db: Session, user_id: int, **kwargs):
    utilisateur = get_utilisateur(db, user_id)
    if not utilisateur:
        return None
    for key, value in kwargs.items():
        setattr(utilisateur, key, value)
    db.commit()
    db.refresh(utilisateur)
    return utilisateur

def delete_utilisateur(db: Session, user_id: int):
    utilisateur = get_utilisateur(db, user_id)
    if utilisateur:
        db.delete(utilisateur)
        db.commit()
        return True
    return False


# ----------------------
# CRUD pour Charge
# ----------------------
def create_charge(db: Session, price: float):
    new_charge = Charge(price=price)
    db.add(new_charge)
    db.commit()
    db.refresh(new_charge)
    return new_charge

def get_charge(db: Session, charge_id: int):
    return db.query(Charge).filter(Charge.charge_id == charge_id).first()

def get_charges(db: Session):
    return db.query(Charge).all()

def update_charge(db: Session, charge_id: int, **kwargs):
    charge = get_charge(db, charge_id)
    if not charge:
        return None
    for key, value in kwargs.items():
        setattr(charge, key, value)
    db.commit()
    db.refresh(charge)
    return charge

def delete_charge(db: Session, charge_id: int):
    charge = get_charge(db, charge_id)
    if charge:
        db.delete(charge)
        db.commit()
        return True
    return False


# ----------------------
# CRUD pour Transaction
# ----------------------
def create_transaction(db: Session, user_id: int, charge_id: int):
    new_transaction = Transaction(user_id=user_id, charge_id=charge_id)
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

def get_transaction(db: Session, transaction_id: int):
    return db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()

def get_transactions(db: Session):
    return db.query(Transaction).all()

def update_transaction(db: Session, transaction_id: int, **kwargs):
    transaction = get_transaction(db, transaction_id)
    if not transaction:
        return None
    for key, value in kwargs.items():
        setattr(transaction, key, value)
    db.commit()
    db.refresh(transaction)
    return transaction

def delete_transaction(db: Session, transaction_id: int):
    transaction = get_transaction(db, transaction_id)
    if transaction:
        db.delete(transaction)
        db.commit()
        return True
    return False