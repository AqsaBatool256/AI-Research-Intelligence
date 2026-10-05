# 🧠 AI Research Intelligence Platform

An AI-powered research assistant that allows users to upload PDF research documents, index their content, ask questions, and receive grounded AI answers with document and page-level source citations.

## ✨ Features

- 📄 Upload and process research PDFs
- 🔎 Extract text while preserving page numbers
- ✂️ Intelligent text chunking
- 🧠 ChromaDB vector search
- 🤖 Gemini-powered research answers
- 📚 Multiple research document support
- 📑 Document and page-level source citations
- 📊 Research knowledge-base statistics
- 📂 Indexed research document library
- ⚡ FastAPI backend
- 🎨 Interactive Streamlit dashboard

## 🛠️ Tech Stack

- Python
- Streamlit
- FastAPI
- Google Gemini API
- ChromaDB
- PyMuPDF
- Python-dotenv
- Requests

## 🏗️ Architecture

```text
User
  │
  ▼
Streamlit Frontend
  │
  ▼
FastAPI Backend
  │
  ├── PDF Extraction
  │
  ├── Text Chunking
  │
  ├── ChromaDB Retrieval
  │
  └── Gemini AI
          │
          ▼
   Grounded Research Answer
          │
          ▼
   Document + Page Sources