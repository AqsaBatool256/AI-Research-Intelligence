from fastapi import FastAPI

from app.api.research import router as research_router


app = FastAPI(
    title="AI Research Intelligence API",
    description="AI-powered research document analysis and question answering API.",
    version="1.0.0",
)


app.include_router(
    research_router,
    prefix="/research",
)


@app.get("/")
def home():
    return {"message": "AI Research Intelligence API is running!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
