1️⃣ Project Title

Resume RAG System using Endee Vector Database

2️⃣ Problem Statement

Recruiters and systems struggle to query resumes intelligently. This project builds a Retrieval-Augmented Generation (RAG) system that allows natural language querying over resume data using vector search.

3️⃣ Architecture Flow

User Question
      ↓
SentenceTransformer Embedding
      ↓
Query sent to Endee Vector DB
      ↓
Top Matching Resume Chunks Retrieved
      ↓
Context passed to LLM
      ↓
Final Answer Generated

4️⃣ Tech Stack

Python
SentenceTransformers (all-MiniLM-L6-v2)
Endee Vector Database
FastAPI (if used in app.py)
Requests
PyPDF

5️⃣ How to Run
# Clone repo
git clone https://github.com/AasthaSharma1809/resume-rag-endee.git
cd resume-rag-endee

# Create venv
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start Endee server separately

# Ingest resume
python ingest.py

# Start app
python app.py

6️⃣ Example Query
Question: What are my technical skills?
Answer: Python, Machine Learning, Data Structures, etc.
