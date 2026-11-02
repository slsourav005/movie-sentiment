
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Movie Review Sentiment API")

# Allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the fine-tuned model from Hugging Face
MODEL_ID = "slsourav005/movie-sentiment"

classifier = pipeline(
    "sentiment-analysis",
    model=MODEL_ID,
    tokenizer=MODEL_ID
)

class TextRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {
        "status": "Server is running",
        "message": "Use /predict for sentiment analysis"
    }

@app.post("/predict")
def predict(request: TextRequest):
    prediction = classifier(request.text)[0]

    label = prediction["label"]
    confidence = float(prediction["score"])

    sentiment = "Positive" if label == "LABEL_1" else "Negative"

    return {
        "sentiment": sentiment,
        "confidence": confidence
    }
