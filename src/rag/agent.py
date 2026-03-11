import logging
import os
from typing import Any, Dict, Optional

from dotenv import load_dotenv
from langchain_classic.chains import RetrievalQA
from langchain_groq import ChatGroq

from .retriever import get_retriever

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

DEFAULT_LLM_MODEL = "llama-3.1-8b-instant"


def ask_question(query: str) -> Optional[Dict[str, Any]]:
    logger.info(f"Received query for RAG processing: '{query}'")

    if not query.strip():
        logger.warning("Empty query received.")
        return None

    if not os.environ.get("GROQ_API_KEY"):
        logger.error("GROQ_API_KEY missing from .env file.")
        return None

    try:
        retriever = get_retriever()

        if not retriever:
            logger.error("Retriever initialization failed.")
            return None

        logger.info(f"Initializing Groq model: {DEFAULT_LLM_MODEL}")

        llm = ChatGroq(
            model=DEFAULT_LLM_MODEL,
            temperature=0
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True
        )

        response = qa_chain.invoke({"query": query})

        return {
            "answer": response.get("result", ""),
            "sources": [
                doc.metadata for doc in response.get("source_documents", [])
            ]
        }

    except Exception as e:
        logger.error(f"Error while answering question: {str(e)}", exc_info=True)
        return None