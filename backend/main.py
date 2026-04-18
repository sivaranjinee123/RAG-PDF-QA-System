# backend/main.py

from fastapi import FastAPI, UploadFile, File, Body
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from pdf_loader import load_pdf
from rag_pipeline import split_docs
from vector_store import store_vectors
from qa_pipeline import ask_question

load_dotenv()

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # later change to http://localhost:3000
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "RAG Backend Running"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        content = await file.read()

        docs = load_pdf(content)
        chunks = split_docs(docs)

        if not chunks:
            return {"error": "No text found in PDF"}

        store_vectors(chunks)

        return {
            "message": "Document uploaded successfully",
            "total_chunks": len(chunks)
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

        return {"answer": answer}

    except Exception as e:
        return {"error": str(e)}