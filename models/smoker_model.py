from sqlalchemy import Column, Integer, String
from models.base import Base

class Smoker(Base):
    __tablename__ = "smoker"
    id_smoker = Column(Integer, primary_key=True, index=True)
    is_smoker = Column(String, nullable=False)