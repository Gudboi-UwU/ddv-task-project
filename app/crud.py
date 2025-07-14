from sqlalchemy.orm import Session
from sqlalchemy import func, extract
from . import models
from datetime import datetime

# Query total dan rata-rata transaksi per kota
def get_city_summary(db: Session):
    return db.query(
        models.Transaction.city,
        func.sum(models.Transaction.amount).label("total_amount"),
        func.avg(models.Transaction.amount).label("average_amount")
    ).group_by(models.Transaction.city).all()

# Query total transaksi, total amount, dan average per merchant
def get_merchant_summary(db: Session):
    return db.query(
        models.Transaction.merchant,
        func.count().label("total_transaction"),
        func.sum(models.Transaction.amount).label("total_amount"),
        func.avg(models.Transaction.amount).label("average_amount")
    ).group_by(models.Transaction.merchant).all()

# Query total amount per bulan per merchant
def get_monthly_totals_by_merchant(db: Session):
    merchants = ["electronic city", "ikea", "periplus", "uniqlo"]

    # Ambil semua bulan unik dari transaksi
    months = db.query(
        extract("year", models.Transaction.transaction_date).label("year"),
        extract("month", models.Transaction.transaction_date).label("month")
    ).distinct().all()

    result = []
    for year, month in months:
        row = {
            "month": f"{int(year):04d}-{int(month):02d}"
        }
        for merchant in merchants:
            total = db.query(func.sum(models.Transaction.amount)).filter(
                models.Transaction.merchant == merchant,
                extract("year", models.Transaction.transaction_date) == year,
                extract("month", models.Transaction.transaction_date) == month
            ).scalar() or 0.0
            row[f"{merchant.lower().replace(' ', '_')}_total_amount"] = total
        result.append(row)
    return result

# Query cumulative amount per merchant per bulan
def get_monthly_cumulative_amount(db: Session):
    # Ambil semua transaksi, urutkan
    txs = db.query(
        models.Transaction.transaction_date,
        models.Transaction.merchant,
        models.Transaction.amount
    ).order_by(models.Transaction.transaction_date).all()

    cumulative = {}
    result = []

    for tx in txs:
        month = tx.transaction_date.replace(day=1)
        merchant = tx.merchant
        key = (month, merchant)
        cumulative[key] = cumulative.get(key, 0) + tx.amount

        total_until_now = sum(
            amount for (m, merch), amount in cumulative.items()
            if m <= month and merch == merchant
        )

        result.append({
            "month": month.isoformat(),
            "merchant": merchant,
            "cumulative_amount": total_until_now
        })

    return result
