from pathlib import Path

from app.services.chunking_service import chunk_pages
from app.services.pdf_service import extract_pdf_pages
from app.services.vector_store import add_chunks


UPLOAD_DIR = Path("data/uploads")


def process_pdf(
    file_path: str,
    document_name: str,
) -> dict:
    """Extract, chunk, and index an uploaded PDF."""

    pages = extract_pdf_pages(file_path)

    if not pages:
        raise ValueError("No readable text was found in the PDF.")

    chunks = chunk_pages(pages)

    if not chunks:
        raise ValueError("No text chunks could be created from the PDF.")

    add_chunks(
        chunks=chunks,
        document_name=document_name,
    )

    return {
        "document": document_name,
        "pages": len(pages),
        "chunks": len(chunks),
    }
