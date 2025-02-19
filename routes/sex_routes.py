from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modules.database import get_db
from models.sex_model import Sex

router = APIRouter()

@router.post("/")
def create_sex(type: str, db: Session = Depends(get_db)):
    sex = Sex(type=type)
    db.add(sex)
    db.commit()
    db.refresh(sex)
    return sex

@router.get("/")
def read_sexes(db: Session = Depends(get_db)):
    sexes = db.query(Sex).all()
    return sexes

@router.get("/{sex_id}")
def read_sex(sex_id: int, db: Session = Depends(get_db)):
    sex = db.query(Sex).filter(Sex.sex_id == sex_id).first()
    if not sex:
        raise HTTPException(status_code=404, detail="Sex not found")
    return sex

@router.put("/{sex_id}")
def update_sex(sex_id: int, type: str, db: Session = Depends(get_db)):
    sex = db.query(Sex).filter(Sex.sex_id == sex_id).first()
    if not sex:
        raise HTTPException(status_code=404, detail="Sex not found")
    sex.type = type
    db.commit()
    db.refresh(sex)
    return sex

@router.delete("/{sex_id}")
def delete_sex(sex_id: int, db: Session = Depends(get_db)):
    sex = db.query(Sex).filter(Sex.sex_id == sex_id).first()
    if not sex:
        raise HTTPException(status_code=404, detail="Sex not found")
    db.delete(sex)
    db.commit()
    return {"detail": "Sex deleted successfully"}