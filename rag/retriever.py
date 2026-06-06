import faiss
import pickle
from sentence_transformers import SentenceTransformer

index = faiss.read_index("data/faiss.index")

with open("data/chunks.pkl", "rb") as f:
    metadata = pickle.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve(query, top_k=5):
    query_vec = model.encode([query])
    distances, indices = index.search(query_vec, top_k)

    results = [metadata[i]["text"] for i in indices[0]]
    return results
