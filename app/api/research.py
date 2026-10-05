from pathlib import Path

from fastapi import APIRouter, File, UploadFile

from app.services.document_service import process_pdf
from app.services.rag_service import answer_research_question
from app.services.vector_store import (
    get_collection_stats,
    get_indexed_documents,
)


router = APIRouter()


# =========================
# UPLOAD DIRECTORY
# =========================

UPLOAD_DIR = Path("data/uploads")

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True,
)


# =========================
# UPLOAD RESEARCH DOCUMENT
# =========================


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
):
    """Upload and index a research PDF."""

    if not file.filename.lower().endswith(".pdf"):
        return {"error": "Only PDF files are supported."}

    file_path = UPLOAD_DIR / file.filename

    content = await file.read()

    file_path.write_bytes(content)

    result = process_pdf(
        file_path=str(file_path),
        document_name=file.filename,
    )

    return {
        "message": "Document indexed successfully.",
        **result,
    }


# =========================
# ASK RESEARCH QUESTION
# =========================


@router.get("/ask")
def ask_research(
    question: str,
):
    """Ask a question about indexed research documents."""

    return answer_research_question(
        question=question,
        limit=5,
    )


# =========================
# RESEARCH STATISTICS
# =========================


@router.get("/stats")
def research_stats():
    """Return statistics about the research knowledge base."""

    return get_collection_stats()


# =========================
# INDEXED DOCUMENTS
# =========================


@router.get("/documents")
def indexed_documents():
    """Return all indexed research documents."""

    return {"documents": get_indexed_documents()}
