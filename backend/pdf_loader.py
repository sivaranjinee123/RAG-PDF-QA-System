from langchain_community.document_loaders import PyPDFLoader
import tempfile

def load_pdf(file_bytes):
    # Save PDF temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name

    # Load PDF
    loader = PyPDFLoader(tmp_path)
    documents = loader.load()

    return documents