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

def analyze_reviews(chunks):
    context = "\n".join(chunks)

    prompt = f"""
You are a customer insights analyst.

Analyze the following customer reviews and provide:

1. Overall sentiment (Positive / Negative / Mixed)
2. Top 3 complaint themes
3. Key improvement suggestions

Reviews:
{context}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
