# Movie Review Sentiment Analysis

An end-to-end NLP project that classifies movie reviews as **Positive** or **Negative** using a fine-tuned BERT model.

## Features

- Fine-tuned BERT (`bert-base-cased`) for sentiment classification.
- FastAPI backend for serving predictions.
- React-based frontend for user interaction.
- Confidence score returned with every prediction.
- Model hosted on Hugging Face.

## Tech Stack

- **Machine Learning:** Python, PyTorch, Hugging Face Transformers
- **Backend:** FastAPI, Pydantic
- **Frontend:** React, HTML, Tailwind CSS
- **Model:** BERT (`bert-base-cased`)
- **Dataset:** IMDb Movie Reviews

## Project Structure

```text
movie-sentiment/
├── backend/
│   ├── main.py
│   └── requirements.txt
├── frontend/
│   └── index.html
├── notebooks/
│   ├── README.md
│   └── model_training.ipynb
├── .gitignore
└── README.md
```

## Model

The fine-tuned model is available on Hugging Face:

[View Movie Sentiment Model](https://huggingface.co/slsourav005/movie-sentiment)

## API Endpoint

**POST** `/predict`

Request:

```json
{
  "text": "This movie was amazing!"
}
```

Response:

```json
{
  "sentiment": "Positive",
  "confidence": 0.98
}
```

*The confidence value above is an illustrative example.*

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/slsourav005/movie-sentiment.git
cd movie-sentiment
```

### 2. Install backend dependencies

```bash
pip install -r backend/requirements.txt
```

### 3. Start the FastAPI server

```bash
uvicorn backend.main:app --reload
```

### 4. Open the frontend

Open `frontend/index.html` in your browser and connect it to the running backend.

## Future Improvements

- Deploy the backend and frontend.
- Improve model evaluation and add performance metrics.
- Add support for batch predictions.
