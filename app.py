from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
import faiss

app= FastAPI()

# ─── Load RAG pipeline on startup ───
print("Loading RAG pipeline...")

loader=PyPDFLoader("10 RAG Architectures.pdf")
documents= loader.load()

splitter=RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks= splitter.split_documents(documents)
embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

vectorstore= FAISS.from_documents(chunks,embeddings)
retirever= vectorstore.as_retriever(search_kwargs={"k":3})

llm= ChatGrog (
    model="llma-3.3-70b-versatile"
    temperature=0,
    api_key="your_groq_api_key"
)

print("RAG pipeline ready!")

# ─── Pydantic models ───
class QueryRequest(BaseModel):
    question: str
    k: Optional[int] = 3

class QueryResponse(BaseModel):
    question: str
    answer: str
    source_chunks: int

# ─── RAG endpoint ───
@app.get("/")
def home():
    return {"message": "RAG API is running!"}

@app.post("/ask", response_model=QueryResponse)
async def ask_question(request: QueryRequest):
    # Step 1 - retrieve relevant chunks
    chunks = retriever.invoke(request.question)
    context = "\n".join([c.page_content for c in chunks])

    # Step 2 - build prompt
    prompt = f"""
You are an expert on RAG architectures.
Use ONLY the context below to answer.
If not in context, say "I don't know."

Context: {context}
Question: {request.question}
Answer:
"""
    # Step 3 - get LLM answer
    response = llm.invoke(prompt)

    return QueryResponse(
        question=request.question,
        answer=response.content,
        source_chunks=len(chunks)
    )