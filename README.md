# E-Commerce End-to-End Data Pipeline (Databricks + Snowflake + Power BI)

## Project Overview
Built an automated, production-grade data pipeline to process daily e-commerce transactional data. The pipeline leverages Databricks and the Medallion Architecture (Bronze, Silver, Gold layers) for scalable data transformation, syncs aggregated metrics to Snowflake, and serves real-time dashboards in Power BI.

---

## Architecture Flow
Local Data Generator / Raw Files 
   └─► Databricks Workflows (PySpark & Delta Lake)
         ├─► Bronze Layer (Raw Ingestion)
         ├─► Silver Layer (Data Cleaning & Deduplication)
         └─► Gold Layer (Business Aggregations)
               └─► Snowflake Data Warehouse (via Python Connector)
                     └─► Power BI Analytics Dashboard

---

## Key Features & Tech Stack
* **Processing & Automation:** PySpark, Databricks Workflows, Python
* **Data Storage:** Delta Lake (Medallion Pattern)
* **Data Warehousing:** Snowflake (`MY_ECOMMERCE_DB`)
* **Analytics:** Power BI Desktop
* **Pipeline Logic:** Implemented `TRUNCATE` & `INSERT` logic using `snowflake-connector-python` to ensure clean, non-duplicated daily data refreshes.
* **Scale:** Handles 7,000+ daily order transactions seamlessly.

---

## Repository Structure
* **`01_pipeline_code.py`**: Contains the end-to-end PySpark ingestion, cleaning, aggregation, and Snowflake loading logic.
* **`README.md`**: Project documentation and setup overview.

---

## Author
* **Ohedul Islam**
  *Data Engineering Student & Practitioner*
