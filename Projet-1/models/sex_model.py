from sqlalchemy import Column, Integer, String
from models.base import Base


class Sex(Base):
    __tablename__ = "sex"
    id_sex = Column(Integer, primary_key=True, index=True)
    sex_label = Column(String, nullable=False)  # noqa: E261, W292