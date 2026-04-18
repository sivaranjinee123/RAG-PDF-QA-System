from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Global in-memory database
db = None

# Load embeddings once (important for speed)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

def store_vectors(chunks):
    """
    Convert document chunks into vectors and store in FAISS
    """
    global db

    if not chunks:
        raise ValueError("No chunks found to store.")

    db = FAISS.from_documents(chunks, embeddings)

    return {
        "message": "Vectors stored successfully",
        "chunks_indexed": len(chunks)
    }


def get_db():
    """
    Return FAISS database
    """
    return db