from pydantic import BaseModel
from datetime import date, time

# Skema jika kita ingin mengirim atau menerima 1 transaksi lengkap (optional)
class TransactionSchema(BaseModel):
    transaction_id: str
    city: str
    amount: float
    merchant: str
    account_id: int
    transaction_date: date
    transaction_time: time

    class Config:
        orm_mode = True

# Skema untuk endpoint Get City Transaction Summary
class CitySummary(BaseModel):
    city: str
    total_amount: float
    average_amount: float

# Skema untuk endpoint Get Merchant Transaction Summary
class MerchantSummary(BaseModel):
    merchant: str
    total_transaction: int
    total_amount: float
    average_amount: float

# Skema untuk Monthly Total by Merchant
class MonthlyMerchantSummary(BaseModel):
    month: str
    electronic_city_total_amount: float
    ikea_total_amount: float
    periplus_total_amount: float
    uniqlo_total_amount: float

# Skema untuk Monthly Cumulative Amount
class MonthlyCumulative(BaseModel):
    month: str
    merchant: str
    cumulative_amount: float
