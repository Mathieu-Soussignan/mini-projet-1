from sqlalchemy import Column, Integer, String
from models.base import Base

class AppUser(Base):
    __tablename__ = "app_user"
    id_user = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    user_email = Column(String, unique=True, nullable=False)