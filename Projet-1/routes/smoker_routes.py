from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modules.database import get_db
from models.smoker_model import Smoker

router = APIRouter()

@router.post("/")
def create_smoker(is_smoker: str, db: Session = Depends(get_db)):
    new_smoker = Smoker(is_smoker=is_smoker)
    db.add(new_smoker)
    db.commit()
    db.refresh(new_smoker)
    return new_smoker

@router.get("/")
def read_smokers(db: Session = Depends(get_db)):
    smokers = db.query(Smoker).all()
    return smokers

@router.get("/{smoker_id}")
def read_smoker(smoker_id: int, db: Session = Depends(get_db)):
    smoker = db.query(Smoker).filter(Smoker.id_smoker == smoker_id).first()
    if not smoker:
        raise HTTPException(status_code=404, detail="Smoker not found")
    return smoker

@router.put("/{smoker_id}")
def update_smoker(smoker_id: int, is_smoker: str, db: Session = Depends(get_db)):
    smoker = db.query(Smoker).filter(Smoker.id_smoker == smoker_id).first()
    if not smoker:
        raise HTTPException(status_code=404, detail="Smoker not found")
    smoker.is_smoker = is_smoker
    db.commit()
    db.refresh(smoker)
    return smoker

@router.delete("/{smoker_id}")
def delete_smoker(smoker_id: int, db: Session = Depends(get_db)):
    smoker = db.query(Smoker).filter(Smoker.id_smoker == smoker_id).first()
    if not smoker:
        raise HTTPException(status_code=404, detail="Smoker not found")
    db.delete(smoker)
    db.commit()
    return {"detail": "Smoker deleted successfully"}