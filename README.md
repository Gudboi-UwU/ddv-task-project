# 🚀 DDV API Project

Project yang dibuat untuk menyelesaikan task rekrutment DDV
Project FastAPI dengan PostgreSQL yang dijalankan menggunakan Docker

---

## 📦 Tech Stack


|     Teknologi     |
|-------------------|
| **FastAPI**       |
| **PostgreSQL**    |
| **Docker**        |
| **Docker Compose**|
| **pgAdmin**       | 
| **Pandas**        | 
| **SQLAlchemy**    | 

---

## 📁 Project Structure
```
fastapi-task/
├── app/                  # Kode utama API
│   ├── crud.py           # Fungsi-fungsi CRUD dari database
│   ├── database.py       # Koneksi ke database
│   ├── main.py           # Start Point
│   ├── models.py         # Struktur tabel database
│   └── schemas.py        # Format data untuk keluar masuk API
│
├── scripts/
│   ├── init_db.sql       # Perintah SQL untuk membuat tabel
│   └── import_csv.py     # Program untuk mengimpor data dari CSV ke PostgreSQL
│
├── transaction_history.csv   # File sumber (CSV)
├── Dockerfile            # Perintah membangun image API
├── docker-compose.yml    # Jalankan semua layanan sekaligus
├── .env.example          # Template env
├── requirements.txt      # Kebutuhan lib python
└── README.md             # Dokumentasi proyek 
```

## 🚀 Running Program

### 1. Install:
- Git
- Docker Desktop

---

### 2. Clone repository

```bash
git clone https://github.com/Gudboi-UwU/ddv-task-project.git
cd ddv-task-project
```

---

### 3. Copy env and edit

```bash
cp .env.example .env
```

Edit file `.env` dan isi sesuai keperluan:


### 4. Run the PostgreSQL on Docker

```bash
docker compose up -d db
```

---

### 5. Create table in PostgreSQL

```bash
type scripts\init_db.sql | docker exec -i postgres_container psql -U user -d transactions_db
```

---

### 6. Import CSV data to the DB

```bash
docker compose run importer
```

---

### 7. Run the FastAPI

```bash
docker compose up -d api
```



## 📌 Endpoints

### 📍 `/city-summary`
- Ringkasan jumlah & rata-rata transaksi berdasarkan kota

### 📍 `/merchant-summary`
- Ringkasan jumlah transaksi & rata-rata transaksi berdasarkan merchant

### 📍 `/monthly-merchant-summary`
- Total transaksi tiap bulan per merchant

### 📍 `/monthly-cumulative`
- Jumlah transaksi yang terus bertambah setiap bulan per merchant

---