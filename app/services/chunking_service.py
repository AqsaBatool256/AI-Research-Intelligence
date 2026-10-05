def chunk_pages(
    pages: list[dict],
    chunk_size: int = 1000,
    overlap: int = 150,
) -> list[dict]:
    """Split extracted PDF pages into overlapping text chunks."""

    chunks = []

    for page in pages:
        text = page["text"]
        page_number = page["page"]

        start = 0

        while start < len(text):
            end = start + chunk_size

            chunk_text = text[start:end].strip()

            if chunk_text:
                chunks.append(
                    {
                        "text": chunk_text,
                        "page": page_number,
                    }
                )

            start += chunk_size - overlap

    return chunks
