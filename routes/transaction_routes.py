from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modules.database import get_db
from models.transaction_model import Transaction

router = APIRouter()

@router.post("/")
def create_transaction(user_id: int, charge_id: int, db: Session = Depends(get_db)):
    transaction = Transaction(user_id=user_id, charge_id=charge_id)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

@router.get("/")
def read_transactions(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    return transactions

@router.get("/{transaction_id}")
def read_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@router.put("/{transaction_id}")
def update_transaction(
    transaction_id: int,
    user_id: int = None,
    charge_id: int = None,
    db: Session = Depends(get_db)
):
    transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    if user_id is not None:
        transaction.user_id = user_id
    if charge_id is not None:
        transaction.charge_id = charge_id
    db.commit()
    db.refresh(transaction)
    return transaction

@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.transaction_id == transaction_id).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    db.delete(transaction)
    db.commit()
    return {"detail": "Transaction deleted successfully"}