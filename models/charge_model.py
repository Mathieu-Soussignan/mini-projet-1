from sqlalchemy import Column, Integer, Float
from models.base import Base

class Charge(Base):
    __tablename__ = "charge"

    charge_id = Column(Integer, primary_key=True, index=True)
    price = Column(Float, nullable=False)