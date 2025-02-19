from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modules.database import get_db
from models.charge_model import Charge

router = APIRouter()

@router.post("/")
def create_charge(price: float, db: Session = Depends(get_db)):
    charge = Charge(price=price)
    db.add(charge)
    db.commit()
    db.refresh(charge)
    return charge

@router.get("/")
def read_charges(db: Session = Depends(get_db)):
    charges = db.query(Charge).all()
    return charges

@router.get("/{charge_id}")
def read_charge(charge_id: int, db: Session = Depends(get_db)):
    charge = db.query(Charge).filter(Charge.charge_id == charge_id).first()
    if not charge:
        raise HTTPException(status_code=404, detail="Charge not found")
    return charge

@router.put("/{charge_id}")
def update_charge(charge_id: int, price: float, db: Session = Depends(get_db)):
    charge = db.query(Charge).filter(Charge.charge_id == charge_id).first()
    if not charge:
        raise HTTPException(status_code=404, detail="Charge not found")
    charge.price = price
    db.commit()
    db.refresh(charge)
    return charge

@router.delete("/{charge_id}")
def delete_charge(charge_id: int, db: Session = Depends(get_db)):
    charge = db.query(Charge).filter(Charge.charge_id == charge_id).first()
    if not charge:
        raise HTTPException(status_code=404, detail="Charge not found")
    db.delete(charge)
    db.commit()
    return {"detail": "Charge deleted successfully"}