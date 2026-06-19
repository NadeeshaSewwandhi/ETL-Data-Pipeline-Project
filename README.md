# ETL-Data-Pipeline-Project
# ETL Data Pipeline Project (Python + PostgreSQL)

An end-to-end ETL (Extract, Transform, Load) pipeline built using Python that extracts data from a REST API, transforms it using Pandas, and loads it into a PostgreSQL database for analysis and reporting.

---

## Project Overview

This project demonstrates a modular ETL pipeline that:

- Extracts product and user data from a REST API (Fake Store API)
- Cleans and transforms raw JSON data into structured datasets
- Loads processed data into PostgreSQL tables
- Follows a scalable ETL architecture used in real-world data engineering workflows

The pipeline automates data ingestion and prepares data for downstream analytics and reporting.

---

## Architecture

```text
        ┌──────────────────────────┐
        │      REST API            │
        │    (Fake Store API)      │
        └──────────┬───────────────┘
                   │
                   ▼
        ┌──────────────────────────┐
        │      EXTRACT LAYER       │
        │ requests + JSON Parsing  │
        │ DataFrame Conversion     │
        └──────────┬───────────────┘
                   │
                   ▼
        ┌──────────────────────────┐
        │     TRANSFORM LAYER      │
        │ Pandas Data Processing   │
        │ • Rename Columns         │
        │ • Flatten JSON           │
        │ • Type Conversion        │
        │ • Data Cleaning          │
        └──────────┬───────────────┘
                   │
                   ▼
        ┌──────────────────────────┐
        │       LOAD LAYER         │
        │ SQLAlchemy + PostgreSQL  │
        │ Store Structured Data    │
        └──────────┬───────────────┘
                   │
                   ▼
        ┌──────────────────────────┐
        │   PostgreSQL Database    │
        │ Products & Users Tables  │
        └──────────────────────────┘
```

---

##  Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Pandas | Data transformation and cleaning |
| Requests | API integration |
| SQLAlchemy | Database connection and ORM |
| PostgreSQL | Data storage |
| Fake Store API | Data source |

---

##  Project Structure

```text
etl-pipeline/
│
├── main.py
│
└── etl/
    ├── extract.py
    ├── transform.py
    └── load.py
```

---

##  ETL Workflow

### 1️⃣ Extract

- Fetches product and user data from Fake Store API
- Validates API responses
- Converts JSON responses into Pandas DataFrames

### 2️⃣ Transform

Data processing includes:

- Column renaming and standardization
- Nested JSON flattening
- Data type conversion
- Selection of relevant attributes
- Data cleaning and structuring

### 3️⃣ Load

- Connects to PostgreSQL database
- Automatically creates/replaces tables
- Loads transformed data using SQLAlchemy

##  Database Configuration

Update PostgreSQL credentials inside `load.py`:

```python
host = "localhost"
port = 5432
user = "postgres"
password = "your_password"
db_name = "store_db"
```

Make sure PostgreSQL is running before executing the pipeline.

---

## ▶️ Run the Pipeline

```bash
python main.py
```

---

##  Output Tables

###  Products Table

| Column |
|----------|
| product_id |
| product_name |
| product_price |
| product_category |
| description |

###  Users Table

| Column |
|----------|
| user_id |
| user_email |
| username |
| first_name |
| last_name |
| street |
| city |
| zipcode |

---

##  Key Features

- Modular ETL architecture
- REST API integration
- Automated data ingestion
- Data cleaning and transformation using Pandas
- Nested JSON flattening
- PostgreSQL database integration
- Reusable and scalable pipeline design
- API response validation and error handling

---

##  Skills Demonstrated

- Data Engineering Fundamentals
- ETL Pipeline Development
- Python Programming
- REST API Integration
- Data Cleaning & Transformation
- Database Management
- SQLAlchemy
- PostgreSQL
- Data Modeling

---

##  Learning Outcomes

Through this project, I gained hands-on experience with:

- Designing ETL pipelines
- Consuming data from REST APIs
- Transforming and cleaning semi-structured JSON data
- Database connectivity using SQLAlchemy
- Loading data into relational databases
- Building modular and maintainable Python applications

---

##  Future Improvements

- Incremental data loading
- Logging and monitoring
- Scheduling with Apache Airflow
- Docker containerization
- Data quality validation checks
- Unit testing for ETL components

---

## 
Author

**Nadeesha**

Data Science & AI Enthusiast | Data Engineering Learner
