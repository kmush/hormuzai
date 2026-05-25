from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from sqlalchemy.sql import func
from .database import Base
from datetime import datetime

class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    url = Column(String, unique=True, index=True)
    summary = Column(Text, nullable=True)
    full_text = Column(Text, nullable=True)
    language = Column(String(10), nullable=True)
    source_country = Column(String(50), nullable=True)
    published_at = Column(DateTime, default=datetime.utcnow)
    sentiment_score = Column(Float)
    key_entities = Column(String)
    discourse_notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())