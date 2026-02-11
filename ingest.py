from sentence_transformers import SentenceTransformer
import requests
import uuid
from pypdf import PdfReader

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load PDF
reader = PdfReader("data/resume.pdf")

text = ""
for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text + "\n"

# Split into chunks
chunks = text.split("\n\n")

print(f"Total Chunks: {len(chunks)}")

for chunk in chunks:
    if chunk.strip() == "":
        continue

    embedding = model.encode(chunk).tolist()

    data = {
        "id": str(uuid.uuid4()),
        "vector": embedding,
        "metadata": {
            "text": chunk
        }
    }

    response = requests.post(
        "http://localhost:8000/upsert",
        json=data
    )

    print("Status:", response.status_code)

print("Ingestion Complete!")
