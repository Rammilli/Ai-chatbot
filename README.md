# AI News Data Pipeline + RAG AI Chatbot

## Project Overview

This project contains two integrated systems:

1. AI News Data Pipeline
2. Retrieval-Augmented Generation (RAG) AI Chatbot

The system collects live news data from RSS feeds, processes articles through multiple NLP stages, stores them in SQLite, and also supports document-based question answering using FAISS vector search and Groq LLM.

---

## Project Structure

```text
Ai-chatbot/
│
├── src/
│   ├── pipeline/
│   │   ├── collector.py
│   │   ├── parser.py
│   │   ├── classifier.py
│   │   ├── dedup.py
│   │   ├── storage.py
│   │   ├── scheduler.py
│   │   └── main.py
│   │
│   ├── rag/
│   │   ├── loader.py
│   │   ├── chunker.py
│   │   ├── embeddings.py
│   │   ├── retriever.py
│   │   ├── agent.py
│   │   └── ask.py
│
├── data/
├── requirements.txt
├── README.md
└── .env