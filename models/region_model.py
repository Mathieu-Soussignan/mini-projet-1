from sqlalchemy import Column, Integer, String
from models.base import Base

class Region(Base):
    __tablename__ = "region"

    region_id = Column(Integer, primary_key=True, index=True)
    region_name = Column(String, nullable=False)