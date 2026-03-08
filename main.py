from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow grader requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SentimentRequest(BaseModel):
    sentences: List[str]

positive_words = {
    "love","great","awesome","good","happy","excellent","fantastic","amazing",
    "nice","wonderful","best","enjoy","liked","like","positive","brilliant",
    "delight","pleasant","super","cool","perfect","satisfied","glad","excited"
}

negative_words = {
    "hate","bad","terrible","awful","sad","worst","angry","horrible","poor",
    "disappointing","disappointed","annoying","frustrating","problem","issue",
    "negative","upset","pain","fail","failure","broken","boring","sucks"
}

def analyze_sentiment(text: str) -> str:
    text = text.lower()

    pos_score = 0
    neg_score = 0

    for word in positive_words:
        if word in text:
            pos_score += 1

    for word in negative_words:
        if word in text:
            neg_score += 1

    if pos_score > neg_score:
        return "happy"
    elif neg_score > pos_score:
        return "sad"
    else:
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
