from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

print("DEBUG:", os.getenv("GROQ_API_KEY"))

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def route_query(question: str) -> str:
    system_prompt = """
Classify the user question into one of the following categories:

1. SQL → If question asks about numbers, metrics, counts, revenue, orders
2. RAG → If question asks for general business insights or explanation
3. SENTIMENT → If question asks about customer reviews, complaints, satisfaction, feedback

Examples:
- "Total sales?" → SQL
- "Why are customers unhappy?" → SENTIMENT
- "Give business insights" → RAG

Return ONLY one word: SQL / RAG / SENTIMENT
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )

    result = response.choices[0].message.content.strip().upper()

    if "SQL" in result:
        return "SQL"
    elif "RAG" in result:
        return "RAG"
    else:
        return "HYBRID"
if __name__ == "__main__":
    tests = [
        "What are the top 5 product categories by revenue?",
        "What do customers complain about most?",
        "What are the reviews saying about top selling products?",
        "How many orders were delivered late?",
        "What is the sentiment around electronics products?",
        "What is the total payment value?",
        "How many orders were placed?",
        "What is the average payment value?",
        "Which seller has the highest revenue?",
        "What are the top 10 product categories by sales?",
        "How many customers are there?",
        "Which state has the most orders?",
        "What is the total freight value?",
        "How many orders were delivered late?",
        "Which payment type is used most?",
        "What do customers complain about most?",
        "Summarize customer reviews",
        "What are customers saying about delivery?",
        "What are the common complaints?",
        "Summarize negative reviews",
        "What is the customer sentiment?",
        "What do customers think about product quality?",
        "What delivery issues are mentioned?",
        "Why are customers unhappy?",
        "Summarize positive feedback",
        "What are customers saying about top selling products?",
        "Why do high selling products receive poor ratings?",
        "Which product categories have high sales but negative reviews?",
        "Compare sales and customer satisfaction",
        "What are the reviews for the highest revenue products?",
        "Which sellers have the most revenue and what complaints do customers have?",
        "Analyze sales and reviews together",
        "Which products have the highest sales and lowest ratings?",
        "Compare ratings and revenue by category"
]
    

    for q in tests:
        print(f"{route_query(q):8} ← {q}")
