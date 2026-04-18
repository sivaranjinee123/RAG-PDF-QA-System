// app/page.tsx

"use client";

import { useState } from "react";

export default function Home() {
  const BACKEND_URL = "http://127.0.0.1:8000";

  const [file, setFile] = useState<File | null>(null);
  const [uploadMsg, setUploadMsg] = useState("");
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState("");

  const [loadingUpload, setLoadingUpload] = useState(false);
  const [loadingAsk, setLoadingAsk] = useState(false);

  const uploadFile = async () => {
    if (!file) {
      setUploadMsg("Please choose a PDF file.");
      return;
    }

    try {
      setLoadingUpload(true);
      setUploadMsg("");

      const formData = new FormData();
      formData.append("file", file);

      const res = await fetch(`${BACKEND_URL}/upload`, {
        method: "POST",
        body: formData,
      });

      const data = await res.json();

      if (data.error) {
        setUploadMsg(data.error);
      } else {
        setUploadMsg(data.message);
      }
    } catch (error) {
      setUploadMsg("Upload failed.");
    } finally {
      setLoadingUpload(false);
    }
  };

  const askQuestion = async () => {
    if (!query.trim()) return;

    try {
      setLoadingAsk(true);
      setAnswer("");

      const res = await fetch(`${BACKEND_URL}/ask`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          query: query,
        }),
      });

      const data = await res.json();

      if (data.error) {
        setAnswer(data.error);
      } else {
        setAnswer(data.answer);
      }
    } catch (error) {
      setAnswer("Something went wrong.");
    } finally {
      setLoadingAsk(false);
    }
  };

  return (
    <main style={styles.page}>
      <div style={styles.card}>
        <h1 style={styles.title}>RAG PDF Question Answering</h1>

        {/* Upload Section */}
        <div style={styles.section}>
          <h2 style={styles.heading}>Upload PDF</h2>

          <input
            type="file"
            accept=".pdf"
            onChange={(e) => setFile(e.target.files?.[0] || null)}
          />

          <button style={styles.button} onClick={uploadFile}>
            {loadingUpload ? "Uploading..." : "Upload"}
          </button>

          <p style={styles.text}>{uploadMsg}</p>
        </div>

        {/* Ask Section */}
        <div style={styles.section}>
          <h2 style={styles.heading}>Ask Question</h2>

          <textarea
            placeholder="Enter your question..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            style={styles.textarea}
          />

          <button style={styles.button} onClick={askQuestion}>
            {loadingAsk ? "Thinking..." : "Ask"}
          </button>

          <div style={styles.answerBox}>
            <strong>Answer:</strong>
            <p>{answer}</p>
          </div>
        </div>
      </div>
    </main>
  );
}

const styles: any = {
  page: {
    minHeight: "100vh",
    background: "#0f172a",
    color: "white",
    padding: "40px",
    fontFamily: "Arial",
  },
  card: {
    maxWidth: "850px",
    margin: "auto",
    background: "#1e293b",
    padding: "30px",
    borderRadius: "12px",
  },
  title: {
    textAlign: "center",
    marginBottom: "30px",
    fontSize: "32px",
  },
  section: {
    marginBottom: "35px",
  },
  heading: {
    marginBottom: "15px",
    fontSize: "24px",
  },
  button: {
    marginTop: "12px",
    padding: "10px 20px",
    background: "#3b82f6",
    color: "white",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer",
  },
  textarea: {
    width: "100%",
    height: "120px",
    padding: "10px",
    borderRadius: "8px",
    marginTop: "10px",
    resize: "none",
  },
  answerBox: {
    marginTop: "20px",
    padding: "15px",
    background: "#334155",
    borderRadius: "8px",
    lineHeight: "1.6",
  },
  text: {
    marginTop: "10px",
  },
};