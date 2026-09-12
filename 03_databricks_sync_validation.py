from pyspark.sql.functions import col

silver_data = spark.read.table("workspace.default.silver_orders")
gold_data = spark.read.table("workspace.default.gold_category_sales")

print("Total Cleaned Records in Silver Layer:", silver_data.count())
print("Total Aggregated Categories in Gold Layer:", gold_data.count())

sf_gold_data = spark.read.table("snowflake_conn_catalog.public.gold_category_sales")
sf_count = sf_gold_data.count()

print("Total Records in Snowflake Gold Table:", sf_count)

if gold_data.count() == sf_count:
    print("Data Sync Check Passed: Databricks and Snowflake counts match perfectly.")
else:
    print("Data Sync Mismatch Warning!")
