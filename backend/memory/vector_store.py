from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

# In-memory store (v2 simple version)
texts = []
index = faiss.IndexFlatL2(384)

def add_to_memory(text):
    embedding = model.encode([text])
    index.add(np.array(embedding).astype("float32"))
    texts.append(text)

def search_memory(query, k=2):
    if len(texts) == 0:
        return ""

    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding).astype("float32"), k)

    results = [texts[i] for i in I[0] if i < len(texts)]
    return "\n".join(results)
