# AI Engineering Assessment – RAG System + AI News Data Pipeline

## Project Overview

This project implements two complete AI engineering systems as part of the technical assessment:

1. **Retrieval Augmented Generation (RAG) Question Answering System**
2. **AI News Data Pipeline for continuous article ingestion, classification, deduplication, and storage**

The objective is to demonstrate practical understanding of:

* Retrieval Augmented Generation
* Vector embeddings
* Document retrieval pipelines
* Structured AI data engineering
* Production-quality Python project organization
* Modular architecture

---

# Project Structure

```text
Ai-chatbot/

├── README.md
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
│
├── src/
│   ├── rag/
│   │   ├── loader.py
│   │   ├── chunker.py
│   │   ├── embeddings.py
│   │   ├── retriever.py
│   │   ├── agent.py
│   │   ├── ask.py
│   │
│   ├── pipeline/
│   │   ├── collector.py
│   │   ├── parser.py
│   │   ├── classifier.py
│   │   ├── storage.py
│   │   ├── dedup.py
│   │   ├── scheduler.py
│   │   ├── main.py
│
│   └── utils/
│
├── data/
│   ├── documents/
│   ├── vector_store/
│   ├── news_pipeline.db
│
├── sample_output/
├── demo/
├── tests/
```

---

# Task 1 – Retrieval Augmented Generation (RAG)

## Objective

Build a document-based question answering system using vector retrieval and LLM generation.

---

## RAG Architecture

```text
Documents → Chunking → Embeddings → FAISS Vector Store → Retrieval → LLM Answer Generation
```

---

## Implemented Components

### loader.py

Loads documents from:

* PDF files
* TXT files
* Local knowledge documents

---

### chunker.py

Splits large documents into semantic chunks using LangChain text splitters.

---

### embeddings.py

Creates embeddings using vector embedding model and stores them in FAISS.

---

### retriever.py

Retrieves most relevant chunks based on query similarity.

---

### agent.py

Combines retrieved context with LLM prompt for answer generation.

---

### ask.py

CLI interface for querying the RAG system.

---

## Run RAG System

```bash
python -m src.rag.ask
```

Example:

```text
Question: What is machine learning?
```

---

## Example Output

```text
Answer:
Machine learning is a field of AI where systems learn patterns from data.

Sources:
document_1.pdf
document_2.txt
```

---

# Task 2 – AI News Data Pipeline

## Objective

Continuously collect public news articles, parse content, classify topics, remove duplicates, and store results.

---

# Pipeline Architecture

```text
RSS Collection → Parsing → Classification → Deduplication → SQLite Storage
```

---

# Implemented Modules

## collector.py

Collects articles from RSS feeds:

* BBC News
* TechCrunch
* The Hindu

---

## parser.py

Extracts clean article content using newspaper3k.

---

## classifier.py

Classifies articles using zero-shot transformer model:

```text
facebook/bart-large-mnli
```

Categories:

* politics
* technology
* sports
* business
* entertainment

---

## dedup.py

Prevents duplicate entries using:

* article_url
* title fallback

---

## storage.py

Stores processed articles in SQLite database.

Table fields:

* title
* source_name
* source_url
* article_url
* published_date
* collected_date
* parsed_content
* category

---

## scheduler.py

Supports repeated execution using schedule library.

---

## main.py

Runs full pipeline:

```bash
python -m src.pipeline.main
```

---

# Example Pipeline Output

```text
Collected: 30 articles
Parsed: 30 articles
Classified: 30 articles
Deduplicated: 30 articles
Stored: 30 rows
```

---

# Libraries Used

## Core Libraries

* Python
* LangChain
* FAISS
* Transformers
* feedparser
* newspaper3k
* sqlite3
* schedule

---

## AI Models

* facebook/bart-large-mnli
* Embedding model for vector generation

---

# Setup Instructions

## Create virtual environment

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment file

Create `.env`

Example:

```env
GOOGLE_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
```

---

# Run Full Project

## Run RAG

```bash
python -m src.rag.ask
```

---

## Run Pipeline

```bash
python -m src.pipeline.main
```

---

# Design Decisions

## Why FAISS?

Chosen because:

* fast local vector retrieval
* lightweight
* no external database dependency

---

## Why SQLite?

Chosen because:

* zero setup
* assignment-friendly
* lightweight local storage

---

## Why Zero-Shot Classification?

Chosen because:

* avoids manual keyword rules
* supports multiple categories dynamically

---

# Assumptions

* RSS feeds remain publicly available
* internet access available during execution
* article URLs remain accessible

---

# Limitations

* transformer classification is slower on CPU
* article parsing depends on source HTML consistency
* scheduler currently local only

---

# Future Improvements

* Add hash-based deduplication
* Add author extraction
* Add language detection
* Add FastAPI interface
* Add PostgreSQL storage
* Add dashboard UI

---

# Demo Deliverables

Included:

* RAG query demo
* pipeline execution demo
* SQLite verification
* sample outputs

---

# Author

Assessment submission by Raman Chinimilli
