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
From the reviews below, extract ONLY the main issues.

Rules:
- Return ONLY 4 to 5 points
- Each point must be short
- Format: issue → fix
- Max 20 words per line
- No explanations
- No extra text
- Output in English

Example:
- Late delivery → fix: Improve logistics speed

Reviews:
{context}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()
