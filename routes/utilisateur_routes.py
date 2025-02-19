from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modules.database import get_db
from models.utilisateur_model import Utilisateur

router = APIRouter()

@router.post("/")
def create_utilisateur(
    user_name: str,
    age: int = None,
    bmi: float = None,
    children: int = None,
    smoker: str = None,
    sex_id: int = None,
    region_id: int = None,
    db: Session = Depends(get_db)
):
    # Vérification minimale : sex_id et region_id sont obligatoires
    if sex_id is None or region_id is None:
        raise HTTPException(status_code=400, detail="sex_id and region_id are required")
    new_user = Utilisateur(
        user_name=user_name,
        age=age,
        bmi=bmi,
        children=children,
        smoker=smoker,
        sex_id=sex_id,
        region_id=region_id
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/")
def read_utilisateurs(db: Session = Depends(get_db)):
    utilisateurs = db.query(Utilisateur).all()
    return utilisateurs

@router.get("/{user_id}")
def read_utilisateur(user_id: int, db: Session = Depends(get_db)):
    utilisateur = db.query(Utilisateur).filter(Utilisateur.user_id == user_id).first()
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return utilisateur

@router.put("/{user_id}")
def update_utilisateur(
    user_id: int,
    user_name: str = None,
    age: int = None,
    bmi: float = None,
    children: int = None,
    smoker: str = None,
    sex_id: int = None,
    region_id: int = None,
    db: Session = Depends(get_db)
):
    utilisateur = db.query(Utilisateur).filter(Utilisateur.user_id == user_id).first()
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    if user_name is not None:
        utilisateur.user_name = user_name
    if age is not None:
        utilisateur.age = age
    if bmi is not None:
        utilisateur.bmi = bmi
    if children is not None:
        utilisateur.children = children
    if smoker is not None:
        utilisateur.smoker = smoker
    if sex_id is not None:
        utilisateur.sex_id = sex_id
    if region_id is not None:
        utilisateur.region_id = region_id
    db.commit()
    db.refresh(utilisateur)
    return utilisateur

@router.delete("/{user_id}")
def delete_utilisateur(user_id: int, db: Session = Depends(get_db)):
    utilisateur = db.query(Utilisateur).filter(Utilisateur.user_id == user_id).first()
    if not utilisateur:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    db.delete(utilisateur)
    db.commit()
    return {"detail": "Utilisateur deleted successfully"}