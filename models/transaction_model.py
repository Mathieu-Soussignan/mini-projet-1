from sqlalchemy import Column, Integer, ForeignKey
from models.base import Base

class Transaction(Base):
    __tablename__ = "transaction"

    transaction_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("utilisateur.user_id"), nullable=False)
    charge_id = Column(Integer, ForeignKey("charge.charge_id"), nullable=False)