import pymupdf


def extract_pdf_pages(file_path: str) -> list[dict]:
    """Extract text from a PDF while preserving page numbers."""

    document = pymupdf.open(file_path)

    pages = []

    for page_number, page in enumerate(document, start=1):
        text = page.get_text("text").strip()

        if text:
            pages.append(
                {
                    "page": page_number,
                    "text": text,
                }
            )

    document.close()

    return pages
