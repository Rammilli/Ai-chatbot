import logging
from pathlib import Path
from typing import Optional, Union

from langchain_community.vectorstores import FAISS
from langchain_core.vectorstores import VectorStoreRetriever

from .embeddings import DEFAULT_VECTOR_STORE_DIR, get_embeddings_model

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

DEFAULT_TOP_K = 3


def get_retriever(
    vector_store_dir: Union[str, Path] = DEFAULT_VECTOR_STORE_DIR,
    top_k: int = DEFAULT_TOP_K
) -> Optional[VectorStoreRetriever]:

    store_path = Path(vector_store_dir)

    logger.info(f"Attempting to load FAISS vector store from: '{store_path}'")

    if not store_path.exists() or not store_path.is_dir():
        logger.error(f"Vector store directory not found at: '{store_path}'")
        return None

    if top_k <= 0:
        logger.warning("top_k must be greater than 0. Using default value 3.")
        top_k = DEFAULT_TOP_K

    try:
        embeddings_model = get_embeddings_model()

        logger.info("Loading local FAISS index from disk...")

        vector_store = FAISS.load_local(
            folder_path=str(store_path),
            embeddings=embeddings_model,
            allow_dangerous_deserialization=True
        )

        retriever = vector_store.as_retriever(
            search_kwargs={"k": top_k}
        )

        logger.info("Retriever successfully configured and ready for queries.")

        return retriever

    except Exception as e:
        logger.error(
            f"An error occurred while loading vector store: {str(e)}",
            exc_info=True
        )
        return None