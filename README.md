# AI Email Suggested Response System

## Overview

This project is a Retrieval-Augmented Generation (RAG) based AI Email Suggested Response System developed as part of the Hiver AI Intern Build Challenge.

The system takes an incoming customer email, retrieves the most similar historical emails using semantic search, generates an AI-powered suggested response using Google's Gemini LLM, and evaluates the generated response using multiple accuracy metrics.

---

## Features

- Semantic Search using Sentence Transformers
- FAISS Vector Database for Retrieval
- Gemini LLM for AI Response Generation
- Synthetic Email Dataset
- Automatic Response Evaluation
- Per-response Accuracy Metrics
- Overall System Quality Score

---

## Project Structure

```
email-ai-assistant/

│── app.py
│── requirements.txt
│── README.md
│── .env

├── data/
│   └── emails.csv

├── embeddings/
│   ├── faiss.index
│   └── metadata.pkl

├── services/
│   ├── __init__.py
│   ├── build_index.py
│   ├── generate_dataset.py
│   ├── retrieve.py
│   ├── prompts.py
│   ├── generator.py
│   └── evaluator.py
```

---

# Dataset

The dataset is synthetic and was generated to simulate real-world customer support conversations.

It contains customer emails paired with their ideal human-written responses.

The dataset includes examples such as:

- Refund requests
- Late deliveries
- Wrong product received
- Damaged products
- Password reset
- Subscription cancellation
- Payment failure
- Address change
- Order tracking

The script `generate_dataset.py` automatically creates the dataset.

---

# Approach

The system follows a Retrieval-Augmented Generation (RAG) pipeline.

### Step 1

Generate embeddings for all customer emails using Sentence Transformers.

↓

### Step 2

Store embeddings inside a FAISS vector index.

↓

### Step 3

Convert the incoming email into an embedding.

↓

### Step 4

Retrieve the Top-3 most similar historical emails.

↓

### Step 5

Provide these retrieved examples to the Gemini LLM as context.

↓

### Step 6

Generate an AI suggested response.

↓

### Step 7

Evaluate the generated response against the reference response.

---

# Technologies Used

- Python
- Google Gemini API
- Sentence Transformers
- FAISS
- Pandas
- Scikit-learn
- NLTK
- ROUGE Score

---

# Evaluation Metrics

The generated response is evaluated using three complementary metrics:

### BLEU Score

Measures word-level similarity between the generated response and the reference response.

### ROUGE-L

Measures sequence overlap and captures how much of the important information is retained.

### Cosine Similarity

Measures semantic similarity between the generated response and the reference response using embeddings.

### Overall Quality Score

The final quality score is calculated as the average of:

- BLEU
- ROUGE-L
- Cosine Similarity

This provides an overall assessment of the generated response quality.

---

# Why These Metrics?

Exact matching alone is too strict for LLM-generated responses because multiple responses can be equally correct while using different wording.

Therefore, a combination of lexical and semantic metrics was used:

- BLEU captures wording similarity.
- ROUGE-L measures content overlap.
- Cosine Similarity measures semantic meaning.

Together they provide a more reliable estimate of response quality.

---

# How to Run

## Install dependencies

```
pip install -r requirements.txt
```

## Generate Dataset

```
python services/generate_dataset.py
```

## Build FAISS Index

```
python services/build_index.py
```

## Run Application

```
python app.py
```

---

# Sample Output

Input

```
Hi, I ordered a laptop 10 days ago but it hasn't arrived yet.
```

Output
Hi, I ordered a laptop 10 days ago but it hasn't arrived yet.

---

# AI Tools Used

The following AI tools were used during development:

- ChatGPT (design discussions, debugging, code refinement)
- Google Gemini API (AI response generation)

---

# Future Improvements

- Larger and more diverse dataset
- Better retrieval ranking
- Hybrid Retrieval (BM25 + Dense Retrieval)
- Human evaluation alongside automatic metrics
- Web-based interface

---

# Author

Smriti Sinha
