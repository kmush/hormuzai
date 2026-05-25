from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import engine, Base, get_db
from . import crud

app = FastAPI(title="Hormuz News API v1.0")

# CORS - Important for Nuxt
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Welcome to the Hormuz News API v1.0. Backend is running and ready to serve!"}

@app.get("/articles")
def read_articles(skip: int = 0, limit: int = 50, lang: str = None, db: Session = Depends(get_db)):
    articles = crud.get_articles(db, skip=skip, limit=limit, language=lang)
    return articles

@app.post("/fetch-news")
async def fetch_news(db: Session = Depends(get_db)):
    return await crud.fetch_and_analyze_news(db)