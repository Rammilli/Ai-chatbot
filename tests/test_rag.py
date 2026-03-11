import pytest
from src.rag.loader import load_documents

def test_load_documents_returns_list():
    """
    Ensure the RAG document ingestion gracefully initiates and
    returns a list of objects, even if the directory is empty.
    """
    documents = load_documents()
    assert isinstance(documents, list)
