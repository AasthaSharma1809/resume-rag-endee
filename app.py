from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from typing import List

app = FastAPI()

# In-memory vector store
database = []

class VectorItem(BaseModel):
    id: str
    vector: List[float]
    metadata: dict

class SearchRequest(BaseModel):
    vector: List[float]
    top_k: int = 3

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

@app.post("/upsert")
def upsert(item: VectorItem):
    database.append(item)
    return {"status": "stored"}

@app.post("/search")
def search(request: SearchRequest):
    query_vec = request.vector
    scored = []

    for item in database:
        sim = cosine_similarity(query_vec, item.vector)
        scored.append((sim, item))

    scored.sort(key=lambda x: x[0], reverse=True)

    results = []
    for score, item in scored[:request.top_k]:
        results.append({
            "score": score,
            "metadata": item.metadata
        })

    return results
