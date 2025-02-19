from sqlalchemy import Column, Integer, String
from models.base import Base

class Sex(Base):
    __tablename__ = "sex"

    sex_id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)