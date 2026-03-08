from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class SentimentRequest(BaseModel):
    sentences: List[str]

positive_words = ["love","great","awesome","good","happy","excellent","amazing"]
negative_words = ["hate","bad","terrible","awful","sad","worst"]

def analyze_sentiment(text: str):
    text = text.lower()

    for w in positive_words:
        if w in text:
            return "happy"

    for w in negative_words:
        if w in text:
            return "sad"

    return "neutral"

@app.post("/sentiment")
def sentiment(data: SentimentRequest):
    results = []

    for sentence in data.sentences:
        results.append({
            "sentence": sentence,
            "sentiment": analyze_sentiment(sentence)
        })

    return {"results": results}
