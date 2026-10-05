import chromadb


# =========================
# CHROMADB CLIENT
# =========================

client = chromadb.PersistentClient(path="data/chroma_db")


collection = client.get_or_create_collection(name="research_documents")


# =========================
# ADD DOCUMENT CHUNKS
# =========================


def add_chunks(
    chunks: list[dict],
    document_name: str,
) -> None:
    """Store document chunks and their metadata in ChromaDB."""

    documents = []
    metadatas = []
    ids = []

    for index, chunk in enumerate(chunks):
        documents.append(chunk["text"])

        metadatas.append(
            {
                "document": document_name,
                "page": chunk["page"],
            }
        )

        ids.append(f"{document_name}_{index}")

    collection.upsert(
        documents=documents,
        metadatas=metadatas,
        ids=ids,
    )


# =========================
# SEARCH DOCUMENT CHUNKS
# =========================


def search_chunks(
    query: str,
    limit: int = 5,
) -> list[dict]:
    """Search for the most relevant document chunks."""

    results = collection.query(
        query_texts=[query],
        n_results=limit,
    )

    matches = []

    if not results["documents"]:
        return matches

    for index, document in enumerate(results["documents"][0]):
        matches.append(
            {
                "text": document,
                "document": results["metadatas"][0][index]["document"],
                "page": results["metadatas"][0][index]["page"],
            }
        )

    return matches


# =========================
# COLLECTION STATISTICS
# =========================


def get_collection_stats() -> dict:
    """Return statistics about the indexed research knowledge base."""

    total_chunks = collection.count()

    if total_chunks == 0:
        return {
            "documents": 0,
            "pages": 0,
            "chunks": 0,
        }

    data = collection.get(include=["metadatas"])

    metadatas = data.get("metadatas", [])

    documents = {
        metadata["document"]
        for metadata in metadatas
        if metadata and "document" in metadata
    }

    pages = {
        (
            metadata["document"],
            metadata["page"],
        )
        for metadata in metadatas
        if metadata and "document" in metadata and "page" in metadata
    }

    return {
        "documents": len(documents),
        "pages": len(pages),
        "chunks": total_chunks,
    }


# =========================
# INDEXED DOCUMENT LIBRARY
# =========================


def get_indexed_documents() -> list[dict]:
    """Return a list of indexed research documents."""

    data = collection.get(include=["metadatas"])

    metadatas = data.get("metadatas", [])

    documents = {}

    for metadata in metadatas:
        if not metadata:
            continue

        document_name = metadata.get("document")

        page = metadata.get("page")

        if not document_name:
            continue

        if document_name not in documents:
            documents[document_name] = {
                "document": document_name,
                "pages": set(),
            }

        if page is not None:
            documents[document_name]["pages"].add(page)

    result = []

    for document in documents.values():
        result.append(
            {
                "document": document["document"],
                "pages": len(document["pages"]),
                "status": "Indexed",
            }
        )

    result.sort(key=lambda item: item["document"].lower())

    return result
