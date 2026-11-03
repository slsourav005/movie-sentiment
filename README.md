# Movie Review Sentiment Analysis

Paste in a movie review, and this app tells you whether it's positive or negative, plus how sure it is about that.

Under the hood, it's a `bert-base-cased` model fine-tuned on IMDb reviews, served with FastAPI, with a small React frontend on top. I built it to learn the whole path from training a model to getting it in front of a user.

## What's inside

- A fine-tuned BERT classifier for positive/negative sentiment
- A FastAPI backend with a single `/predict` endpoint
- A React + Tailwind frontend for trying reviews in the browser
- A confidence score with every prediction
- The trained model on Hugging Face, so there's no need to retrain it: [slsourav005/movie-sentiment](https://huggingface.co/slsourav005/movie-sentiment)

## Built with

- **ML:** Python, PyTorch, Hugging Face Transformers
- **Backend:** FastAPI, Pydantic
- **Frontend:** React, HTML, Tailwind CSS
- **Data:** IMDb Movie Reviews

## Project layout

```
movie-sentiment/
├── backend/
│   ├── main.py              # FastAPI app and prediction logic
│   └── requirements.txt
├── frontend/
│   └── index.html           # The UI
├── notebooks/
│   ├── README.md
│   └── model_training.ipynb # How the model was fine-tuned
├── .gitignore
└── README.md
```
```bash
## Try it locally


# 1. Clone the repo
git clone - https://github.com/slsourav005/movie-sentiment.git
cd movie-sentiment

# 2. Install backend dependencies
pip install -r backend/requirements.txt

# 3. Start the server
uvicorn backend.main:app --reload
```

Then open `frontend/index.html` in your browser. Keep the server running so the page can reach it.

## Using the API

Send a `POST` request to `/predict`:

```json
{ "text": "This movie was amazing!" }
```

You'll get back:

```json
{ "sentiment": "Positive", "confidence": 0.98 }
```

The confidence value here is just an example. Real scores will vary with the input.

## Still on my to-do list

- Deploy the backend and frontend so people can try it without setting anything up
- Properly evaluate the model and report accuracy, precision, recall, and F1
- Support batch predictions

## About

Made by [Sourav Shil](https://github.com/slsourav005). Feedback and suggestions are welcome.

