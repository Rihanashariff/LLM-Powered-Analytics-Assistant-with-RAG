import pandas as pd
import sqlite3
import os

DATA_PATH="data/"
DB_PATH="data/olist.db"

def load_data():
    conn = sqlite3.connect(DB_PATH)

    #Load Data
    customers = pd.read_csv(os.path.join(DATA_PATH, "olist_customers_dataset.csv"))
    geolocations = pd.read_csv(os.path.join(DATA_PATH, "olist_geolocation_dataset.csv"))
    orders = pd.read_csv(os.path.join(DATA_PATH, "olist_orders_dataset.csv"))
    order_items = pd.read_csv(os.path.join(DATA_PATH, "olist_order_items_dataset.csv"))
    reviews = pd.read_csv(os.path.join(DATA_PATH, "olist_order_reviews_dataset.csv"))
    products = pd.read_csv(os.path.join(DATA_PATH, "olist_products_dataset.csv"))
    sellers = pd.read_csv(os.path.join(DATA_PATH, "olist_sellers_dataset.csv"))
    payments = pd.read_csv(os.path.join(DATA_PATH, "olist_order_payments_dataset.csv"))

    print("All CSV files loaded")

    #Data Cleaning
     # Orders - convert date columns
    date_cols = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date"
    ]

    for col in date_cols:
        if col in orders.columns:
            orders[col] = pd.to_datetime(orders[col], errors='coerce')

       # Reviews - clean text
    reviews["review_comment_message"] = reviews["review_comment_message"].fillna("No Review")
    reviews["review_comment_message"] = reviews["review_comment_message"].str.lower()

     # Products - fill missing category
    products["product_category_name"] = products["product_category_name"].fillna("unknown")

    # Customers - fill missing city/state
    customers["customer_city"] = customers["customer_city"].fillna("unknown")

    # Payments - fill missing values
    payments["payment_type"] = payments["payment_type"].fillna("unknown")

    print("Data cleaning completed")

    #SAVE CLEAN TABLES
    customers.to_sql("customers", conn, if_exists="replace", index=False)
    geolocations.to_sql("geolocations", conn, if_exists="replace", index=False)
    orders.to_sql("orders", conn, if_exists="replace", index=False)
    order_items.to_sql("order_items", conn, if_exists="replace", index=False)
    reviews.to_sql("order_reviews", conn, if_exists="replace", index=False)
    products.to_sql("products", conn, if_exists="replace", index=False)
    sellers.to_sql("sellers", conn, if_exists="replace", index=False)
    payments.to_sql("payments", conn, if_exists="replace", index=False)
    
    print("All tables saved to database")

    #Merge all Tables into one for easier retrieval

    df = orders.merge(customers, on="customer_id", how="left")
    df = df.merge(order_items, on="order_id", how="left")
    df = df.merge(products, on="product_id", how="left")
    df = df.merge(reviews, on="order_id", how="left")
    df = df.merge(payments, on="order_id", how="left")
    df = df.merge(sellers, on="seller_id", how="left")

    #remove duplicates
    df = df.drop_duplicates()

    #Save Merged table
    df.to_sql("final_dataset", conn, if_exists="replace", index=False)

    print("Final combined dataset created successfully!")

    conn.close()

if __name__ == "__main__":
    load_data()


