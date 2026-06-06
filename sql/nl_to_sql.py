from openai import OpenAI
import sqlite3
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

print("DEBUG:", os.getenv("GROQ_API_KEY"))

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

DB_PATH = "data/olist.db"

SCHEMA = """
Tables:
orders(order_id, customer_id, order_status, order_purchase_timestamp)
order_items(order_id, product_id, price)
order_reviews(review_id, order_id, review_score, review_comment_message)
products(product_id, product_category_name)
customers(customer_id, customer_city)
payments(order_id, payment_type, payment_value)
"""

# 🔹 1. Generate SQL
def generate_sql(query):
    prompt = f"""
You are an expert SQLite query generator.

Convert the user question into a correct SQLite query.

Rules:
- Use only given tables
- Use proper JOINs when needed
- Do not explain, only return SQL

{SCHEMA}

Question: {query}

SQL:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content.strip()


# 🔹 2. Execute SQL
def execute_sql(sql):
    conn = sqlite3.connect(DB_PATH)

    try:
        df = pd.read_sql(sql, conn)
    except Exception as e:
        print("❌ SQL Error:", e)
        return pd.DataFrame()

    finally:
        conn.close()

    return df


# 🔹 3. Summarize result
def summarize(df):
    if df.empty:
        return "No data found."

    prompt = f"""
You are a business analyst.

Explain the following data in simple business insights:

{df.head(10).to_string(index=False)}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
