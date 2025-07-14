from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

# Buat semua tabel berdasarkan model ORM
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency untuk koneksi DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/summary/city", response_model=list[schemas.CitySummary])
def city_summary(db: Session = Depends(get_db)):
    return crud.get_city_summary(db)

@app.get("/summary/merchant", response_model=list[schemas.MerchantSummary])
def merchant_summary(db: Session = Depends(get_db)):
    return crud.get_merchant_summary(db)

@app.get("/summary/monthly-merchant", response_model=list[schemas.MonthlyMerchantSummary])
def monthly_by_merchant(db: Session = Depends(get_db)):
    return crud.get_monthly_totals_by_merchant(db)

@app.get("/summary/monthly-cumulative", response_model=list[schemas.MonthlyCumulative])
def monthly_cumulative(db: Session = Depends(get_db)):
    return crud.get_monthly_cumulative_amount(db)
