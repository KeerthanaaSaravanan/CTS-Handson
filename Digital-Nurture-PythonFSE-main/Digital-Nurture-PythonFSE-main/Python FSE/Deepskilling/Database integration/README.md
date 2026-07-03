# Database Integration — Digital Nurture 5.0

> **Module 3 · Python Full Stack Engineering (FSE) · Deep Skilling Program**

This module covers end-to-end database integration skills using **MySQL**, **MongoDB**, **SQLAlchemy ORM**, and **Alembic migrations**. It is structured across 7 Hands-On exercises, each building on the previous.

---

## Repository Structure

```
Database Integration/
├── HandsOn-1/          # DDL – Schema Design & Normalization
├── HandsOn-2/          # DML – Data Manipulation & Querying
├── HandsOn-3/          # Advanced SQL – Subqueries, Views, Procedures
├── HandsOn-4/          # Performance – Indexes & N+1 Query Problem
├── HandsOn-5/          # NoSQL – MongoDB Collections & Aggregation
├── HandsOn-6/          # ORM – SQLAlchemy CRUD & Relationships
├── HandsOn-7/          # Migrations – Alembic Schema Versioning
└── DatabaseIntegration_HandsOn.pdf   # Full problem statement PDF
```

---

##  Domain Context

All exercises revolve around a **College Management System** database (`college_db`) with the following entities:

| Table | Description |
|---|---|
| `departments` | Academic departments with budget info |
| `students` | Student records linked to departments |
| `courses` | Courses offered per department |
| `enrollments` | Student–course enrollment records with grades |
| `professors` | Faculty linked to departments with salary info |

---

##  Hands-On Breakdown

---

###  HandsOn-1 — DDL: Schema Design & Normalization

**Technology:** MySQL · **Concepts:** DDL, Data Modeling, Normalization

| File | Description |
|---|---|
| `TablesInput.sql` | Raw schema input / reference table definitions |
| `Task1_Create_Database_and_Tables.sql` | Creates `college_db` with all 5 tables and foreign key constraints |
| `Task2_Normalization_Analysis.txt` | Analysis of 1NF, 2NF, and 3NF compliance across the schema |
| `Task3_Alter_Table.sql` | Schema evolution — `ALTER TABLE` to add/drop columns, rename, and add CHECK constraints |

**Key Concepts:**
- `CREATE DATABASE`, `CREATE TABLE`, `PRIMARY KEY`, `FOREIGN KEY`
- Schema normalization (1NF → 2NF → 3NF)
- `ALTER TABLE`: Add, rename, drop columns; `CHECK` constraints

---

###  HandsOn-2 — DML: Data Manipulation & Basic Querying

**Technology:** MySQL · **Concepts:** DML, Filtering, Joins, Aggregations

| File | Description |
|---|---|
| `Task1_DML.sql` | Bulk `INSERT` for all tables; `UPDATE` grades; `DELETE` NULL records |
| `Task2_Single_Table_Queries.sql` | Filtering with `WHERE`, `LIKE`, `BETWEEN`, `GROUP BY`, `ORDER BY` |
| `Task3_Multi_Table_Joins.sql` | `INNER JOIN`, `LEFT JOIN` across students, courses, departments |
| `Task4_Aggregations.sql` | `COUNT`, `AVG`, `ROUND`; grouping with `HAVING`; grade distribution |

**Key Concepts:**
- `INSERT INTO`, `UPDATE`, `DELETE`
- Single-table filtering, sorting, and grouping
- Multi-table joins
- Aggregate functions: `COUNT`, `AVG`, `MAX`, `MIN`

---

###  HandsOn-3 — Advanced SQL: Subqueries, Views & Stored Procedures

**Technology:** MySQL · **Concepts:** Subqueries, Views, Stored Procedures, Transactions

| File | Description |
|---|---|
| `Task1_Subqueries.sql` | Correlated subqueries, `EXISTS`, `NOT EXISTS`, derived tables |
| `Task2_Views.sql` | Creating and querying views; `WITH CHECK OPTION`; updatable vs. non-updatable views |
| `Task3_Stored_Procedures_and_Transactions.sql` | Stored procedures for enrollment & transfer; `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

**Key Concepts:**
- Scalar, correlated, and derived-table subqueries
- `CREATE VIEW`, `WITH CHECK OPTION`
- `CREATE PROCEDURE`, `DELIMITER`, `SIGNAL SQLSTATE`
- `START TRANSACTION`, `COMMIT`, `ROLLBACK`, `SAVEPOINT`

---

###  HandsOn-4 — Performance: Indexes & N+1 Problem

**Technology:** MySQL + Python (mysql-connector) · **Concepts:** Query Optimization, Indexing, N+1 Anti-pattern

| File | Description |
|---|---|
| `Task1_Baseline_Performance.sql` | `EXPLAIN FORMAT=JSON` for a 3-table join — baseline full table scan analysis |
| `Task2_Indexes.sql` | Creating indexes on `enrollment_year`, `email`, composite index; comparing EXPLAIN output |
| `Task3_N_Plus_One.py` | Demonstrates N+1 query problem vs. optimized single JOIN query in Python |
| `Task3_Observations.txt` | Output comparison: N+1 (13 queries) vs. JOIN (1 query) with timing data |

**Key Concepts:**
- `EXPLAIN FORMAT=JSON` for execution plan analysis
- `CREATE INDEX`, composite indexes
- N+1 Query Anti-pattern — fetching related data in a loop
- Optimization using a single `JOIN` query

>  **Note:** Replace `your_password` in `Task3_N_Plus_One.py` with your actual MySQL password before running.

---

###  HandsOn-5 — NoSQL: MongoDB Collections & Aggregation

**Technology:** MongoDB (mongosh) · **Concepts:** Document Model, CRUD, Aggregation Pipeline

| File | Description |
|---|---|
| `Task1_Create_Collection.js` | Creates `college_nosql` DB, `feedback` collection, inserts 10 sample documents with nested arrays |
| `Task2_CRUD_Operations.js` | Find by rating/tag/course; update ratings; delete low-rating records |
| `Task3_Aggregation_Pipeline.js` | `$group`, `$match`, `$sort`, `$limit`, `$unwind` — average ratings, top courses, tag frequency |

**Key Concepts:**
- MongoDB document model (flexible schema, nested objects/arrays)
- `insertMany`, `find`, `updateOne`, `deleteMany`
- Aggregation pipeline operators: `$group`, `$match`, `$sort`, `$limit`, `$unwind`, `$avg`, `$sum`

---

### HandsOn-6 — ORM: SQLAlchemy CRUD & Relationships

**Technology:** Python + SQLAlchemy · **Concepts:** ORM, Model Classes, Relationships

| File | Description |
|---|---|
| `requirements.txt` | `sqlalchemy`, `pymysql` dependencies |
| `Task1_Setup_ORM.py` | Engine creation, connection test, `declarative_base` setup |
| `Task2_CRUD_ORM.py` | ORM-based `Student` model; Insert, Read (query), Update, Delete via session |
| `Task3_Relationships.py` | `Department` ↔ `Student` one-to-many relationship using `ForeignKey` and `relationship()` |

**Key Concepts:**
- `create_engine`, `sessionmaker`, `declarative_base`
- ORM model classes with `Column`, `Integer`, `String`
- `session.add()`, `session.query()`, `session.commit()`, `session.delete()`
- `ForeignKey`, `relationship()`, `back_populates`

> **Note:** Set your DB password in `DATABASE_URL` before running. Current placeholder: `your_password`

---

###  HandsOn-7 — Migrations: Alembic Schema Versioning

**Technology:** Python + Alembic + SQLAlchemy · **Concepts:** Schema Migration, Version Control for DB

| File | Description |
|---|---|
| `alembic.ini` | Alembic configuration; `sqlalchemy.url` points to `college_db` |
| `requirements.txt` | `alembic`, `sqlalchemy`, `pymysql` dependencies |
| `Task1_Initialize_Alembic.txt` | `alembic init migrations` — output and folder structure explained |
| `Task2_Create_Migration.txt` | `alembic revision -m "..."` — creating migration version files |
| `Task3_Apply_Migration.txt` | `alembic upgrade head` — applying migrations and verifying with `alembic current` |
| `Task4_Rollback_Migration.txt` | `alembic downgrade -1` and `downgrade base` — rollback and migration history |
| `migrations/` | Alembic environment (`env.py`, `script.py.mako`, `versions/`) |

**Alembic Commands Summary:**

```bash
# Initialize
python -m alembic init migrations

# Create a new revision
python -m alembic revision -m "create student table"

# Apply all migrations
python -m alembic upgrade head

# Check current revision
python -m alembic current

# Rollback one step
python -m alembic downgrade -1

# Rollback to beginning
python -m alembic downgrade base

# View history
python -m alembic history
```

>  **Note:** Update `sqlalchemy.url` in `alembic.ini` with your actual DB password before running migrations.

---

## 🛠️ Prerequisites

| Tool | Version |
|---|---|
| Python | 3.10+ |
| MySQL Server | 8.0+ |
| MongoDB | 6.0+ (for HandsOn-5) |
| pip packages | `mysql-connector-python`, `sqlalchemy`, `pymysql`, `alembic` |

---

## ⚙️ Setup Instructions

### 1. MySQL Setup (HandsOn 1–4, 6–7)

```sql
-- Run in MySQL Workbench or CLI
source HandsOn-1/Task1_Create_Database_and_Tables.sql;
source HandsOn-2/Task1_DML.sql;
```

### 2. Python Dependencies (HandsOn 4, 6, 7)

```bash
pip install mysql-connector-python sqlalchemy pymysql alembic
```

### 3. MongoDB Setup (HandsOn-5)

```bash
# Start mongosh and run scripts
mongosh
load("HandsOn-5/Task1_Create_Collection.js")
load("HandsOn-5/Task2_CRUD_Operations.js")
load("HandsOn-5/Task3_Aggregation_Pipeline.js")
```

---

## Security Note

All database passwords in this repository have been replaced with `your_password` as a placeholder.  
**Do NOT commit real credentials to version control.** Use environment variables or a `.env` file in practice.

```python
import os
DATABASE_URL = f"mysql+pymysql://root:{os.environ['DB_PASSWORD']}@localhost/college_db"
```

---

## Author

**Keerthana Saravanan**  
Digital Nurture 5.0 — Python Full Stack Engineering (FSE) Deep Skilling  
Module: Database Integration

---
