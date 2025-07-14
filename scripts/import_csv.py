import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load env dari .env file
load_dotenv()

# Ambil nilai env
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

# Bangun URL koneksi
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_HOST}:{DB_PORT}/{POSTGRES_DB}"
engine = create_engine(DATABASE_URL)

# Baca CSV dan insert ke DB
df = pd.read_csv("data/transaction_history.csv", parse_dates=["transaction_date"])
df.to_sql("transactions", engine, if_exists="append", index=False)

print("Data imported successfully!")