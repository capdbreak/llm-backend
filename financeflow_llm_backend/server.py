from pathlib import Path
from typing import Annotated, List

from pydantic import BaseModel, Field
from fastapi import Body, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from financeflow_llm_backend.core import load_chain, AnalysisResult, Article, NewsArticles, news_chain

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

chain = load_chain()

@app.get("/health")
async def check_health():
    return {"status": "ok"}


@app.post("/analyze")
async def run_query(
    articles: Annotated[List[Article], Body(...)],
    subject: Annotated[str, Body(...)]
) -> AnalysisResult:
    results = []
    for article in articles:
        results.append(chain.invoke(article.dict() | {"subject": subject}))
    
    return {
        "results": results
    }

@app.post("/news")
async def get_news(
    date: Annotated[str, Body(...)],
    num_of_news: Annotated[str, Body(...)],
    subject: Annotated[str, Body(...)]
) -> NewsArticles:
    return news_chain.invoke({"date": date, "numbers": num_of_news, "topic": subject})
