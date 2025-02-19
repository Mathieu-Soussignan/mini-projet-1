from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modules.database import get_db
from models.app_user_model import AppUser

router = APIRouter()

@router.post("/")
def create_app_user(username: str, password: str, user_email: str, db: Session = Depends(get_db)):
    new_app_user = AppUser(username=username, password=password, user_email=user_email)
    db.add(new_app_user)
    db.commit()
    db.refresh(new_app_user)
    return new_app_user

@router.get("/")
def read_app_users(db: Session = Depends(get_db)):
    users = db.query(AppUser).all()
    return users

@router.get("/{user_id}")
def read_app_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(AppUser).filter(AppUser.id_user == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="App user not found")
    return user

@router.put("/{user_id}")
def update_app_user(
    user_id: int,
    username: str = None,
    password: str = None,
    user_email: str = None,
    db: Session = Depends(get_db)
):
    user = db.query(AppUser).filter(AppUser.id_user == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="App user not found")
    if username is not None:
        user.username = username
    if password is not None:
        user.password = password
    if user_email is not None:
        user.user_email = user_email
    db.commit()
    db.refresh(user)
    return user

@router.delete("/{user_id}")
def delete_app_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(AppUser).filter(AppUser.id_user == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="App user not found")
    db.delete(user)
    db.commit()
    return {"detail": "App user deleted successfully"}