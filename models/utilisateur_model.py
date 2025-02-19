from sqlalchemy import Column, Integer, String, Float, ForeignKey
from models.base import Base

class Utilisateur(Base):
    __tablename__ = "utilisateur"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    bmi = Column(Float, nullable=True)
    children = Column(Integer, nullable=True)
    smoker = Column(String, nullable=True)
    sex_id = Column(Integer, ForeignKey("sex.sex_id"), nullable=False)
    region_id = Column(Integer, ForeignKey("region.region_id"), nullable=False)