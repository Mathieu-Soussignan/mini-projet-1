from sqlalchemy import Column, Integer, String, Float, ForeignKey
from models.base import Base

class Patient(Base):
    __tablename__ = "patient"

    id_patient = Column(Integer, primary_key=True, index=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    age = Column(Integer, nullable=True)
    bmi = Column(Float, nullable=True)
    patient_email = Column(String, nullable=True)
    children = Column(Integer, nullable=True)
    charges = Column(Float, nullable=True)

    # Clés étrangères
    sex_id = Column(Integer, ForeignKey("sex.id_sex"), nullable=False)
    region_id = Column(Integer, ForeignKey("region.id_region"), nullable=False)
    smoker_id = Column(Integer, ForeignKey("smoker.id_smoker"), nullable=False)
    user_id = Column(Integer, ForeignKey("app_user.id_user"), nullable=True)