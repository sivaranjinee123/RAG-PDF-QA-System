from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from vector_store import get_db

model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


def ask_question(query):
    db = get_db()

    if db is None:
        return "No documents uploaded yet."

    docs = db.similarity_search_with_score(query, k=5)
    docs = sorted(docs, key=lambda x: x[1])[:3]
    docs = [d[0] for d in docs]

    context = "\n\n".join(doc.page_content for doc in docs)

    prompt = f"""
Use only the context below.

Context:
{context}

Question: {query}

If missing, say I don't know.

Answer:
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)

    outputs = model.generate(
        **inputs,
        max_new_tokens=120,
        do_sample=False
    )

    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return answer.strip()