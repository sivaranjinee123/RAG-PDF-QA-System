# backend/main.py

from fastapi import FastAPI, UploadFile, File, Body
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from pdf_loader import load_pdf
from rag_pipeline import split_docs
from vector_store import store_vectors
from qa_pipeline import ask_question

load_dotenv()

app = FastAPI(
    title="RAG PDF QA API",
    description="Upload PDF and ask questions using RAG",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # change after deploy
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "RAG Backend Running",
        "status": "success"
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        # Validate PDF
        if not file.filename.endswith(".pdf"):
            return {"error": "Only PDF files allowed"}

        content = await file.read()

        docs = load_pdf(content)
        chunks = split_docs(docs)

        if not chunks:
            return {"error": "No text found in PDF"}

        store_vectors(chunks)

        return {
            "message": "Document uploaded successfully",
            "total_chunks": len(chunks),
            "filename": file.filename
        }

    except Exception as e:
        return {"error": str(e)}


@app.post("/ask")
async def ask(data: dict = Body(...)):
    try:
        query = data.get("query", "").strip()

        if not query:
            return {"error": "Query is required"}

        answer = ask_question(query)

        return {
            "query": query,
            "answer": answer
        }

    except Exception as e:
        return {"error": str(e)}