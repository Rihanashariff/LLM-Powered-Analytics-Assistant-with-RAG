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

def synthesize(question,sql_result, rag_result):
    prompt = f"""
Answer the question using the data below.

Question:
{question}

SQL Result:
{sql_result}

Review Insights:
{rag_result}

Rules:
- Give ONLY 3-4 short points
- Focus on direct reasons (not strategy)
- NO recommendations
- NO business expansion ideas
- Keep answer very short

Final Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",   
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
