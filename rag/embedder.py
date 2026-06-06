from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd
import pickle
import sqlite3

DB_PATH = "data/olist.db"

def chunk_text(text, chunk_size=200):
    words = str(text).split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def build_faiss():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT review_id, review_comment_message FROM order_reviews WHERE review_comment_message IS NOT NULL", conn)

    chunks = []
    metadata = []

    for _, row in df.iterrows():
        split_chunks = chunk_text(row["review_comment_message"])
        for chunk in split_chunks:
            chunks.append(chunk)
            metadata.append({"review_id": row["review_id"], "text": chunk})

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(chunks)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)

    faiss.write_index(index, "data/faiss.index")

    with open("data/chunks.pkl", "wb") as f:
        pickle.dump(metadata, f)

    print("FAISS index created!")

if __name__ == "__main__":
    build_faiss()
