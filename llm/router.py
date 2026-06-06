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
    system_prompt = """Classify the question as SQL, RAG, or HYBRID.
Reply ONLY one word."""

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
    ]
    for q in tests:
        print(f"{route_query(q):8} ← {q}")
