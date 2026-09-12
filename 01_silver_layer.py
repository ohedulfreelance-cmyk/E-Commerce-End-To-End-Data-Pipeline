from pyspark.sql.functions import col, to_timestamp, trim, current_timestamp

bronze_df = spark.read.table("snowflake_conn_catalog.public.bronze_orders")

silver_df = (
    bronze_df
    .filter((col("PRICE") > 0) & (col("CUSTOMER_NAME").isNotNull()) & (trim(col("CUSTOMER_NAME")) != ""))
    .withColumn("CUSTOMER_NAME", trim(col("CUSTOMER_NAME")))
    .withColumn("ORDER_TIMESTAMP", to_timestamp(col("ORDER_TIMESTAMP")))
    .dropDuplicates(["ORDER_ID"])
    .withColumn("PROCESSED_AT", current_timestamp())
)

silver_df.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("workspace.default.silver_orders")

print("Silver Layer Execution Successful!")
display(spark.read.table("workspace.default.silver_orders"))
