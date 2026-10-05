from app.services.llm_service import generate_research_answer
from app.services.vector_store import search_chunks


def answer_research_question(
    question: str,
    limit: int = 5,
) -> dict:
    """Retrieve relevant research content and generate an answer."""

    sources = search_chunks(
        query=question,
        limit=limit,
    )

    if not sources:
        return {
            "answer": (
                "I couldn't find enough information in the uploaded research documents."
            ),
            "sources": [],
        }

    answer = generate_research_answer(
        question=question,
        sources=sources,
    )

    return {
        "answer": answer,
        "sources": sources,
    }
