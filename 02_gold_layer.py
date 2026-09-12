from pyspark.sql.functions import sum, count, round, col

silver_df = spark.read.table("workspace.default.silver_orders")

gold_df = (
    silver_df
    .groupBy("PRODUCT_CATEGORY")
    .agg(
        count("ORDER_ID").alias("TOTAL_ORDERS"),
        round(sum("PRICE"), 2).alias("TOTAL_REVENUE")
    )
    .orderBy(col("TOTAL_REVENUE").desc())
)

gold_df.write \
    .format("delta") \
    .mode("overwrite") \
    .option("overwriteSchema", "true") \
    .saveAsTable("workspace.default.gold_category_sales")

print("Gold Layer Aggregation Successful!")
display(spark.read.table("workspace.default.gold_category_sales"))
