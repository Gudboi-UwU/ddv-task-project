from sqlalchemy import Column, String, Float, BigInteger, Date, Time
from .database import Base

# ORM model: representasi tabel "transactions" dalam Python
class Transaction(Base):
    __tablename__ = "transactions"  # Nama tabel di PostgreSQL

    transaction_id = Column(String, primary_key=True, index=True)
    city = Column(String)
    amount = Column(Float)
    merchant = Column(String)
    account_id = Column(BigInteger)
    transaction_date = Column(Date)
    transaction_time = Column(Time)
