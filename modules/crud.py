from sqlalchemy.orm import Session
from models.utilisateur_model import Patient
from models.transaction_model import Cost

# ----------------------
# Patients
# ----------------------
def create_patient(db: Session, first_name: str, last_name: str, age: int = None, bmi: float = None):
    new_patient = Patient(first_name=first_name, last_name=last_name, age=age, bmi=bmi)
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    return new_patient

def get_patient(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()

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


# ----------------------
# Costs
# ----------------------
def create_cost(db: Session, patient_id: int, amount: float):
    new_cost = Cost(patient_id=patient_id, amount=amount)
    db.add(new_cost)
    db.commit()
    db.refresh(new_cost)
    return new_cost

def get_cost(db: Session, cost_id: int):
    return db.query(Cost).filter(Cost.id == cost_id).first()

def get_costs(db: Session):
    return db.query(Cost).all()

def update_cost(db: Session, cost_id: int, **kwargs):
    cost = get_cost(db, cost_id)
    if not cost:
        return None
    for key, value in kwargs.items():
        setattr(cost, key, value)
    db.commit()
    db.refresh(cost)
    return cost

def delete_cost(db: Session, cost_id: int):
    cost = get_cost(db, cost_id)
    if cost:
        db.delete(cost)
        db.commit()
        return True
    return False