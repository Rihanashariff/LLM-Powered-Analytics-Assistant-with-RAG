from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

print("DEBUG:", os.getenv("GROQ_API_KEY"))

# Initialize Groq client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def synthesize(sql_result, rag_result):
    prompt = f"""
You are an e-commerce analytics expert.

Combine structured (SQL) and unstructured (customer reviews) insights.

SQL Result:
{sql_result}

Review Insights:
{rag_result}

Give a clear, concise business insight.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",   
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
