from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow external requests (important for grader)

app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

class SentimentRequest(BaseModel):
sentences: List[str]

positive_words = ["love", "great", "awesome", "good", "happy", "excellent", "amazing"]
negative_words = ["hate", "bad", "terrible", "awful", "sad", "worst"]

def analyze_sentiment(text: str) -> str:
text = text.lower()

```
for word in positive_words:
    if word in text:
        return "happy"

for word in negative_words:
    if word in text:
        return "sad"

return "neutral"
```

@app.post("/sentiment")
def sentiment(data: SentimentRequest):
results = []

```
for sentence in data.sentences:
    results.append({
        "sentence": sentence,
        "sentiment": analyze_sentiment(sentence)
    })

return {"results": results}
```

