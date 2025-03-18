from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modules.database import get_db
from models.patient_model import Patient

router = APIRouter()


@router.post("/")
def create_patient(
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
    user_id: int = None,
    db: Session = Depends(get_db)
):
    # Vérification minimale : sex_id, region_id et smoker_id sont obligatoires
    if sex_id is None or region_id is None or smoker_id is None:
        raise HTTPException(status_code=400, detail="sex_id, region_id and smoker_id are required") # noqa
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


@router.get("/")
def read_patients(db: Session = Depends(get_db)):
    patients = db.query(Patient).all()
    return patients


@router.get("/{patient_id}")
def read_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id_patient == patient_id).first() # noqa
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@router.put("/{patient_id}")
def update_patient(
    patient_id: int,
    last_name: str = None,
    first_name: str = None,
    age: int = None,
    bmi: float = None,
    patient_email: str = None,
    children: int = None,
    charges: float = None,
    sex_id: int = None,
    region_id: int = None,
    smoker_id: int = None,
    user_id: int = None,
    db: Session = Depends(get_db)
):
    patient = db.query(Patient).filter(Patient.id_patient == patient_id).first() # noqa: E501, E261
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    if last_name is not None:
        patient.last_name = last_name
    if first_name is not None:
        patient.first_name = first_name
    if age is not None:
        patient.age = age
    if bmi is not None:
        patient.bmi = bmi
    if patient_email is not None:
        patient.patient_email = patient_email
    if children is not None:
        patient.children = children
    if charges is not None:
        patient.charges = charges
    if sex_id is not None:
        patient.sex_id = sex_id
    if region_id is not None:
        patient.region_id = region_id
    if smoker_id is not None:
        patient.smoker_id = smoker_id
    if user_id is not None:
        patient.user_id = user_id
    db.commit()
    db.refresh(patient)
    return patient


@router.delete("/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = db.query(Patient).filter(Patient.id_patient == patient_id).first() # noqa
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    db.delete(patient)
    db.commit()
    return {"detail": "Patient deleted successfully"} # noqa