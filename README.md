````markdown
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
````

## 🚀 Live Demo

### 🌐 Frontend

[AI Research Intelligence Platform](https://ai-research-intelligence-zqcpbjyjwsva64syxgd8hr.streamlit.app/)

### ⚡ Backend API

[FastAPI Backend](https://ai-research-intelligence-t3do.onrender.com/)

### 📖 API Documentation

[FastAPI Swagger Documentation](https://ai-research-intelligence-t3do.onrender.com/docs)

### ❤️ Backend Health

[Health Check](https://ai-research-intelligence-t3do.onrender.com/health)

## 📁 Project Structure

```text
AI-Research-Intelligence/
│
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   └── research.py
│   │
│   ├── frontend/
│   │   └── streamlit_app.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── chunking_service.py
│   │   ├── document_service.py
│   │   ├── llm_service.py
│   │   ├── pdf_service.py
│   │   ├── rag_service.py
│   │   └── vector_store.py
│   │
│   └── main.py
│
├── data/
│   ├── chroma_db/
│   └── uploads/
│
├── .gitignore
├── README.md
└── requirements.txt
```

## 🔄 How It Works

1. User uploads a PDF research document.
2. FastAPI receives and stores the document.
3. PyMuPDF extracts text while preserving page numbers.
4. Extracted text is divided into overlapping chunks.
5. ChromaDB indexes the document chunks.
6. User submits a research question.
7. Relevant chunks are retrieved from the knowledge base.
8. Gemini generates an answer using the retrieved research context.
9. The application displays the answer together with document and page sources.

## 🔐 Security

* API keys are stored as environment variables.
* `.env` files are excluded from Git.
* Uploaded PDFs are excluded from Git.
* ChromaDB data is excluded from Git.
* Secrets are never stored in source code.

## 💻 Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/AqsaBatool256/AI-Research-Intelligence.git
cd AI-Research-Intelligence
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment on Windows

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never commit the `.env` file to GitHub.

### 6. Start the FastAPI backend

```bash
uvicorn app.main:app --reload
```

### 7. Start the Streamlit frontend

Open another terminal, activate the virtual environment, and run:

```bash
streamlit run app/frontend/streamlit_app.py
```

## ☁️ Deployment

The project is deployed using:

* **Frontend:** Streamlit Community Cloud
* **Backend:** Render
* **Repository:** GitHub

The FastAPI backend provides endpoints for:

* PDF document uploads
* Research questions
* Knowledge-base statistics
* Indexed document information
* Health monitoring

## 🔌 API Endpoints

| Endpoint              | Method | Purpose                               |
| --------------------- | ------ | ------------------------------------- |
| `/`                   | GET    | API status                            |
| `/health`             | GET    | Health check                          |
| `/research/upload`    | POST   | Upload and index a PDF                |
| `/research/ask`       | GET    | Ask a research question               |
| `/research/stats`     | GET    | Get knowledge-base statistics         |
| `/research/documents` | GET    | List indexed documents                |
| `/docs`               | GET    | Interactive Swagger API documentation |

## 🎯 Project Goal

The goal of this project is to demonstrate how Retrieval-Augmented Generation (RAG) can be used to build an intelligent research assistant that answers questions from uploaded documents while maintaining traceability to the original research sources.

## 🔮 Future Improvements

* Multi-document research comparison
* Research paper summarization
* Automatic keyword and topic extraction
* Advanced citation highlighting
* Research analytics dashboard
* Persistent cloud vector storage
* Improved document processing for scanned PDFs
* Conversation history and research sessions

## 👩‍💻 Author

**Aqsa Batool Saqib**

BS Computer Science Student
AI & Machine Learning Enthusiast
Python Developer
Cloud Computing Learner

### Connect

* GitHub: https://github.com/AqsaBatool256
* LinkedIn: https://www.linkedin.com/in/aqsabatoolsaqib/

```

**This is the version I recommend committing.** Save it as `README.md`. Then we can do the Git commands to commit and push it.
```
