from transformers import pipeline
import json

# Load once when module is imported
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_sentiment(text: str):
    if not text or len(text) < 10:
        return {"score": 0.0, "label": "NEUTRAL"}
    result = sentiment_pipeline(text[:512])[0]  # Truncate for speed
    # Convert to -1 to 1 scale
    score = result['score'] if result['label'] == 'POSITIVE' else -result['score']
    return {"score": round(score, 3), "label": result['label']}

def extract_key_entities(text: str):
    # Simple keyword extraction for V1.0
    keywords = ["Iran", "US", "China", "Chinese", "blockade", "tanker", "strait", "sanctions", "military", "navy",
                "oil", "gas", "energy", "Hormuz", "Ormuz", "霍尔木兹", "ホルムズ", "هرمز" ]
    found = [kw for kw in keywords if kw.lower() in text.lower()]
    return list(set(found))

