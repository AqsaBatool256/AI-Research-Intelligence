# 🧠 AI Research Intelligence Platform

An AI-powered research assistant that allows users to upload research papers and PDF documents, ask questions about their content, and receive grounded AI-generated answers with page-level source references.

The platform combines **Retrieval-Augmented Generation (RAG)**, **ChromaDB**, **Google Gemini**, **FastAPI**, and **Streamlit** to create an intelligent research document analysis system.

## 🚀 Live Demo

### Frontend

https://ai-research-intelligence-zqcpbjyjwsva64syxgd8hr.streamlit.app/

### Backend API

https://ai-research-intelligence-t3do.onrender.com/

### API Health Check

https://ai-research-intelligence-t3do.onrender.com/health

## ✨ Features

* 📄 Upload research PDF documents
* 🔎 Extract text from PDF files
* ✂️ Split documents into overlapping text chunks
* 🧠 Store document knowledge using ChromaDB
* 🔍 Retrieve relevant research content using semantic search
* 🤖 Generate AI-powered answers using Google Gemini
* 📚 Provide document and page-level source references
* 📊 Display research knowledge-base statistics
* 📁 View indexed research documents
* 🌙 Modern dark-themed dashboard
* ✨ Animated and responsive Streamlit interface
* ⚡ FastAPI backend for document processing and AI queries
* ☁️ Publicly deployed frontend and backend

## 🛠️ Tech Stack

### Programming Language

* Python

### Frontend

* Streamlit

### Backend

* FastAPI
* Uvicorn

### AI

* Google Gemini API
* Retrieval-Augmented Generation (RAG)

### Document Processing

* PyMuPDF

### Vector Database

* ChromaDB

### Data Validation

* Pydantic

### Development Tools

* Git
* GitHub
* VS Code

### Deployment

* Streamlit Cloud
* Render

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │       User           │
                    │  Upload PDF / Query  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Streamlit Frontend  │
                    │     Dashboard        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    FastAPI Backend   │
                    │  REST API Endpoints  │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴───────────┐
                    ▼                      ▼
          ┌──────────────────┐    ┌──────────────────┐
          │   PDF Processing │    │   Question       │
          │   PyMuPDF        │    │   Processing     │
          └────────┬─────────┘    └────────┬─────────┘
                   │                       │
                   ▼                       ▼
          ┌──────────────────┐    ┌──────────────────┐
          │ Text Chunking    │    │ ChromaDB Search  │
          └────────┬─────────┘    └────────┬─────────┘
                   │                       │
                   ▼                       ▼
          ┌──────────────────────────────────────────┐
          │              ChromaDB                    │
          │        Research Knowledge Base            │
          └────────────────────┬─────────────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Google Gemini     │
                    │   Grounded Answer    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Streamlit Response   │
                    │ + Source References  │
                    └──────────────────────┘
```

## 📂 Project Structure

```text
AI-Research-Intelligence/
│
├── app/
│   ├── __init__.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── research.py
│   │
│   ├── frontend/
│   │   └── streamlit_app.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── chunking_service.py
│       ├── document_service.py
│       ├── llm_service.py
│       ├── pdf_service.py
│       ├── rag_service.py
│       └── vector_store.py
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

### 1. Upload a PDF

The user uploads a research paper or PDF document through the Streamlit dashboard.

### 2. Extract Text

PyMuPDF extracts readable text from each PDF page while preserving page numbers.

### 3. Create Chunks

The extracted text is divided into smaller overlapping chunks to improve retrieval quality.

### 4. Store Knowledge

The chunks and their metadata are stored in ChromaDB.

Each chunk keeps information such as:

* Document name
* Page number
* Extracted text

### 5. Ask a Research Question

The user enters a question about the uploaded research documents.

### 6. Retrieve Relevant Information

ChromaDB searches the indexed research knowledge base and retrieves the most relevant chunks.

### 7. Generate an Answer

The retrieved research content is sent to Google Gemini with instructions to answer only from the provided research context.

### 8. Display Sources

The application displays the generated answer together with the relevant document and page references.

## 🔌 API Endpoints

### Health Check

```text
GET /health
```

Returns:

```json
{
  "status": "healthy"
}
```

### Upload Document

```text
POST /research/upload
```

Uploads and indexes a PDF research document.

### Ask a Research Question

```text
GET /research/ask?question=YOUR_QUESTION
```

Retrieves relevant research content and generates an AI-powered answer.

### Research Statistics

```text
GET /research/stats
```

Returns:

* Number of indexed documents
* Number of indexed pages
* Number of knowledge chunks

### Indexed Documents

```text
GET /research/documents
```

Returns the list of indexed research documents.

## 🔐 Security

API credentials are not stored in the source code.

The Gemini API key is stored securely using environment variables / deployment secrets.

The `.env` file is excluded from Git using `.gitignore`.

```text
.env
.streamlit/secrets.toml
```

No API keys or private credentials are included in the public repository.

## 💻 Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AqsaBatool256/AI-Research-Intelligence.git
cd AI-Research-Intelligence
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API Key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

Do not commit this file to GitHub.

### 6. Start the FastAPI Backend

```bash
uvicorn app.main:app --reload
```

The backend will run locally at:

```text
http://127.0.0.1:8000
```

### 7. Start the Streamlit Frontend

Open another terminal and run:

```powershell
streamlit run app/frontend/streamlit_app.py
```

The Streamlit application will open in your browser.

## ☁️ Deployment

### Backend

The FastAPI backend is deployed using Render.

Production start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

The Gemini API key is configured securely in Render environment variables.

### Frontend

The Streamlit frontend is deployed using Streamlit Cloud.

The frontend connects to the deployed FastAPI backend through the `BACKEND_URL` configuration.

## 📊 Current Capabilities

The platform currently supports:

* PDF upload
* PDF text extraction
* Page-aware document processing
* Text chunking
* ChromaDB indexing
* Semantic retrieval
* Gemini-powered research question answering
* Source references
* Research document library
* Knowledge-base statistics
* Public Streamlit deployment
* Public FastAPI deployment

## 🔮 Future Improvements

Planned improvements include:

* 📑 Automatic research paper summaries
* 🏷️ Keyword and topic extraction
* 📊 Research analytics dashboard
* 📚 Multiple research collections
* 🔎 Advanced document filtering
* 🧠 Improved retrieval and reranking
* 📌 More detailed page-level citations
* 📈 Document comparison
* 📝 Automatic literature review generation
* 📊 Research trend analysis
* 💬 Conversation history
* 🔐 User authentication
* 🎨 Additional UI animations and themes

## 🎯 Project Goal

The goal of this project is to demonstrate how modern AI techniques can transform large research documents into an interactive knowledge system.

Instead of manually searching through long research papers, users can upload their documents and interact with their research knowledge base using natural language.

The project demonstrates practical experience with:

* Artificial Intelligence
* Machine Learning
* Generative AI
* Retrieval-Augmented Generation
* Vector Databases
* Natural Language Processing
* API Development
* Document Processing
* Cloud Deployment

## 👩‍💻 Author

**Aqsa Batool Saqib**

BS Computer Science Student
AI & Machine Learning Enthusiast
Python Developer
Cloud Computing Learner

### Connect

GitHub:
https://github.com/AqsaBatool256

LinkedIn:
https://www.linkedin.com/in/aqsabatoolsaqib/

Portfolio:
https://aqsabatool256.github.io/

---

⭐ If you find this project interesting, feel free to explore the repository and live demo.
