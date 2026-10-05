import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai


PROJECT_ROOT = Path(__file__).resolve().parents[2]

load_dotenv(dotenv_path=PROJECT_ROOT / ".env")


MODEL_NAME = "gemini-3.8-flash"

client = None


def generate_research_answer(
    question: str,
    sources: list[dict],
) -> str:
    """Generate a grounded answer using retrieved research sources."""

    global client

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is not configured.")

    if client is None:
        client = genai.Client(api_key=api_key)

    context_parts = []

    for source in sources:
        context_parts.append(
            f"""
Document: {source["document"]}
Page: {source["page"]}

Content:
{source["text"]}
"""
        )

    context = "\n".join(context_parts)

    prompt = f"""
You are an AI research assistant.

Answer the user's question using ONLY the research content provided below.

Do not invent facts or information.

If the provided research content does not contain enough information
to answer the question, say:

"I couldn't find enough information in the uploaded research documents."

Be clear, accurate, and concise.

Research content:
{context}

User question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
    )

    return response.text.strip()
