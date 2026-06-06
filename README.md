## 🚀 LLM-Powered Analytics Assistant with RAG

An AI-powered analytics system that allows users to query an e-commerce database and customer reviews using natural language. The system combines **LLM-based NL-to-SQL generation**, **Retrieval-Augmented Generation (RAG)**, and **hybrid reasoning** to deliver intelligent, data-driven insights with visualizations.

---

## 📌 Project Overview

Business users often struggle with writing SQL queries and analyzing large volumes of customer reviews. This project solves that problem by building an **LLM-powered assistant** that understands natural language and returns:

- 📊 Structured data insights (via SQL)
- 💬 Customer sentiment insights (via RAG)
- 🔀 Combined hybrid analysis
- 📈 Auto-generated visualizations

It is built using the **Olist Brazilian E-Commerce dataset**.


## 🧠 Key Features

### 🔹 Natural Language to SQL
- Converts English questions into SQLite queries using LLM
- Executes queries on structured e-commerce database
- Returns summarized business insights

### 🔹 Retrieval-Augmented Generation (RAG)
- Processes customer reviews using embeddings
- FAISS-based similarity search
- Sentiment analysis (positive / negative / mixed)
- Extracts key complaint themes

### 🔹 Hybrid Intelligence Engine
- Combines SQL + RAG outputs
- Handles complex analytical questions

### 🔹 Query Router
- Automatically classifies input into:
  - SQL
  - RAG
  - HYBRID

### 🔹 Auto Chart Generator
- Suggests best visualization type (bar, line, pie)
- Generates interactive Plotly charts

### 🔹 Streamlit UI
- Simple web interface
- Real-time query interaction


## 📂 Project Structure
```bash
rag-analytics-assistant/
│
├── data/
│   ├── olist.db                  # SQLite database (Olist e-commerce data)
│   ├── chunks.pkl               # Chunked review text for RAG
│   ├── faiss_index.bin          # FAISS vector index for embeddings
│   └── olist_loader.py          # ETL pipeline (CSV → SQLite)
│
├── rag/
│   ├── embedder.py             # Generate embeddings (Sentence Transformers)
│   └── retriever.py            # FAISS similarity search
│
├── sql/
│   └── nl_to_sql.py            # Natural Language → SQL generator
│
├── llm/
│   ├── router.py               # Classifies query → SQL / RAG / HYBRID
│   ├── sentiment.py            # Sentiment analysis
│   ├── synthesizer.py          # Combines SQL + RAG results
│   └── chart_generator.py     # Auto chart selection + Plotly visualization
│
├── app.py                      # Streamlit UI (main entry point)
│
├── .env                        # API keys (Groq / LLM keys)
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```
## 📦 requirements.txt

Data handling:
pandas
numpy

Embeddings for RAG:
sentence-transformers

Vector database:
faiss-cpu

LLM API (GROQ instead of OpenAI):
groq

Environment variables:
python-dotenv

UI:
streamlit


# 📊 Dataset

| Field   | Detail |
|--------|--------|
| Name   | Brazilian E-Commerce Public Dataset by Olist |
| Source | Kaggle (uploaded to Google Drive per guidelines) |
| Size   | ~100,000 orders · 8 relational tables · ~40,000 review records |
| Period | 2016 – 2018 |
| Format | CSV files loaded into SQLite |

# 💡 Example Queries

# 📊 SQL Queries

What are the top 5 product categories by revenue?
What is the total revenue from all orders?
What is the average delivery time of orders?
Who are the top 10 customers by number of orders?

# 💬RAG Queries

What do customers generally think about delivery service?
Are most reviews positive or negative?
Why do customers give low ratings?
What do customers like about products?

# HYBRID Queries

How does delivery time affect customer satisfaction?
Which product categories have the worst reviews and lowest sales?
re expensive products getting better reviews?


