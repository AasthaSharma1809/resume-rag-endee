import requests
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# Embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Question Answering model (MUCH better than GPT2)
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def search_resume(question):
    query_vector = embed_model.encode(question).tolist()

    response = requests.post(
        "http://localhost:8000/search",
        json={"vector": query_vector, "top_k": 3}
    )

    results = response.json()

    context = " ".join([item["metadata"]["text"] for item in results])
    return context

while True:
    question = input("\nAsk a question about your resume: ")
    if question.lower() in ["exit", "quit"]:
        break

    context = search_resume(question)

    if context.strip() == "":
        print("No relevant resume data found.")
        continue

    result = qa_pipeline(question=question, context=context)
    print("\nAnswer:", result["answer"])
