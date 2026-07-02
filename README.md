# 📄 PDF RAG API using FastAPI

A Retrieval-Augmented Generation (RAG) application built with **FastAPI**, **LangChain**, **FAISS**, **Hugging Face Embeddings**, and **Groq Llama 3.3**.

The API accepts a question, retrieves the most relevant content from a PDF using semantic search, and generates an answer using an LLM.

---

## Features

- Upload and process PDF documents
- Semantic search using FAISS
- Hugging Face sentence-transformer embeddings
- Llama 3.3 via Groq
- FastAPI REST API
- Pydantic request validation

---

## Tech Stack

- Python
- FastAPI
- LangChain
- FAISS
- Hugging Face Embeddings
- Groq API
- Pydantic

---

## Project Structure

```
.
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── 10 RAG Architectures.pdf
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/<your-username>/pdf-rag-fastapi.git
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Key

Set your Groq API key as an environment variable.

Windows (PowerShell)

```powershell
$env:GROQ_API_KEY="your_api_key"
```

Linux / macOS

```bash
export GROQ_API_KEY="your_api_key"
```

Then update your code to read the key from the environment instead of hardcoding it.

---

## Run the API

```bash
uvicorn app:app --reload
```

---

## API Endpoints

### Health Check

```
GET /
```

Response

```json
{
  "message": "RAG API is running!"
}
```

---

### Ask a Question

```
POST /ask
```

Request

```json
{
    "question":"What is Agentic RAG?"
}
```

Response

```json
{
    "question":"What is Agentic RAG?",
    "answer":"...",
    "source_chunks":3
}
```

---

## How It Works

1. Load the PDF
2. Split the document into chunks
3. Generate embeddings using Hugging Face
4. Store embeddings in FAISS
5. Retrieve the most relevant chunks
6. Send the retrieved context and user question to the LLM
7. Return the generated answer

---

## Future Improvements

- Support multiple PDF uploads
- Save FAISS index to disk
- Docker support
- Authentication
- Streaming responses
- Conversation memory

---

## License

This project is for learning and educational purposes.
