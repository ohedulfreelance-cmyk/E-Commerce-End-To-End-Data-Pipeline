import time
import random
from faker import Faker
import snowflake.connector

fake = Faker()

sf_config = {
    "user": "<YOUR_SNOWFLAKE_USER>",
    "password": "<YOUR_SNOWFLAKE_PASSWORD>",
    "account": "<YOUR_SNOWFLAKE_ACCOUNT>",
    "warehouse": "COMPUTE_WH",
    "database": "MY_ECOMMERCE_DB",
    "schema": "PUBLIC"
}

conn = snowflake.connector.connect(**sf_config)
cursor = conn.cursor()

print("Connected to Snowflake Warehouse...")

try:
    while True:
        order_id = fake.uuid4()
        customer_name = fake.name().replace("'", "")
        product_category = random.choice(["Electronics", "Clothing", "Home & Kitchen", "Books", "Beauty"])
        price = round(random.uniform(15.0, 1500.0), 2)
        timestamp = fake.iso8601()

        insert_query = f"""
        INSERT INTO BRONZE_ORDERS (ORDER_ID, CUSTOMER_NAME, PRODUCT_CATEGORY, PRICE, ORDER_TIMESTAMP)
        VALUES ('{order_id}', '{customer_name}', '{product_category}', {price}, '{timestamp}');
        """

        cursor.execute(insert_query)
        print(f"Ingested to Bronze: {customer_name} | {product_category} | ${price}")
        
        time.sleep(3)

except KeyboardInterrupt:
    print("Bronze ingestion process stopped.")

finally:
    cursor.close()
    conn.close()
