# E-Commerce End-to-End Data Pipeline (Databricks + Snowflake + Power BI)

## Project Overview
This project demonstrates an end-to-end, production-ready data engineering pipeline built using the Medallion Architecture (Bronze, Silver, Gold). Real-time e-commerce transaction data is ingested, cleaned, aggregated, and synced with Snowflake for analytical reporting in Power BI.

---

## Pipeline Architecture
1. **Source / Ingestion (Bronze Layer):** Real-time streaming synthetic transaction data generated via Python (`Faker`) and loaded directly into Snowflake.
2. **Data Cleaning (Silver Layer):** Deduplication, NULL value handling, and column standardization performed using PySpark on Databricks.
3. **Data Aggregation (Gold Layer):** Business metric aggregation computed and structured for analytics.
4. **Data Sync & Validation:** Cross-platform record count verification between Databricks Delta tables and Snowflake target data warehouse.
5. **Data Quality Check:** Target-side SQL quality checks executed in Snowflake to ensure zero-null records.

---

## Key Features & Tech Stack
* **Processing & Automation:** PySpark, Databricks Workflows, Python
* **Data Storage:** Delta Lake (Medallion Pattern)
* **Data Warehousing:** Snowflake (`MY_ECOMMERCE_DB`)
* **Analytics:** Power BI Desktop
* **Pipeline Logic:** Implemented real-time streaming, PySpark data cleaning, and Snowflake sync validation.

---

## Repository Structure
* **`00_bronze_layer_ingestion.py`**: Real-time synthetic ingestion script.
* **`01_silver_layer.py`**: Data cleaning and deduplication logic.
* **`02_gold_layer.py`**: Business metrics aggregation logic.
* **`03_databricks_sync_validation.py`**: Cross-platform record count verification.
* **`04_snowflake_data_check.sql`**: Snowflake query-level data quality checks.
* **`README.md`**: Project documentation and setup overview.
