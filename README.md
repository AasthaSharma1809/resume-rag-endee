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

🎯 Use Case: Resume Semantic Search & RAG
This project demonstrates how vector databases can power intelligent resume querying systems for:
AI Resume Screening
HR Tech Platforms
Smart Candidate Search
Context-Aware Resume Q&A

This project uses Endee as the core vector database to store and retrieve high-dimensional embeddings for semantic search and RAG-based question answering.

DEMO OUTPUT
To start the server:

PS C:\Users\aasth> cd C:\Users\aasth\endee\resume-rag-endee
PS C:\Users\aasth\endee\resume-rag-endee> venv\Scripts\activate
(venv) PS C:\Users\aasth\endee\resume-rag-endee> python -m uvicorn app:app --reload
INFO:     Will watch for changes in these directories: ['C:\\Users\\aasth\\endee\\resume-rag-endee']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [14136] using StatReload
INFO:     Started server process [13024]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

Chatbot:
(venv) PS C:\Users\aasth\endee\resume-rag-endee> python chat.py
Ask a question about your resume: What certifications do I have?
Answer: Mastering Data Structures & Algorithms
Ask a question about your resume: what skills do i have?
Answer: problem-solving and programming
