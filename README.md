\# 📄 RAG PDF Question Answering System



!\[Python](https://img.shields.io/badge/Python-3.11-blue)

!\[FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)

!\[Next.js](https://img.shields.io/badge/Next.js-Frontend-black)

!\[FAISS](https://img.shields.io/badge/FAISS-VectorDB-orange)

!\[HuggingFace](https://img.shields.io/badge/HuggingFace-FLAN--T5-yellow)



AI-powered full-stack application that lets users upload PDF documents and ask natural language questions using \*\*Retrieval-Augmented Generation (RAG)\*\*.



\---



\## 🚀 Features



✅ Upload PDF files  

✅ Extract document text  

✅ Semantic search using embeddings  

✅ FAISS vector retrieval  

✅ FLAN-T5 answer generation  

✅ FastAPI backend  

✅ Next.js frontend UI  



\---



\## 🧠 How It Works



1\. Upload PDF  

2\. Extract text  

3\. Split into chunks  

4\. Convert chunks to embeddings  

5\. Store vectors in FAISS  

6\. Ask question  

7\. Retrieve relevant chunks  

8\. Generate answer using FLAN-T5  



\---



\## 🛠 Tech Stack



| Layer | Technology |

|------|------------|

| Frontend | Next.js + TypeScript |

| Backend | FastAPI |

| Embeddings | all-MiniLM-L6-v2 |

| Vector DB | FAISS |

| LLM | google/flan-t5-small |

| Language | Python |



\---



\## 📂 Project Structure



``` id="qsd0p0"

RAG-System/

├── backend/

│   ├── main.py

│   ├── qa\_pipeline.py

│   ├── vector\_store.py

│

├── rag-frontend/

│   ├── app/

│   ├── page.tsx

│

└── README.md

