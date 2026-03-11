import logging
from pathlib import Path
from typing import List, Optional, Union

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

logger = logging.getLogger(__name__)

DEFAULT_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
DEFAULT_VECTOR_STORE_DIR = Path("data/vector_store")

def get_embeddings_model(model_name: str = DEFAULT_MODEL_NAME) -> HuggingFaceEmbeddings:
    """
    Initialize and return the HuggingFace embeddings model.
    
    Args:
        model_name (str, optional): The name of the SentenceTransformers model to use.
            Defaults to "sentence-transformers/all-MiniLM-L6-v2".
            
    Returns:
        HuggingFaceEmbeddings: The initialized embeddings model ready for use.
        
    Raises:
        Exception: Re-raises exceptions if the model fails to load, allowing 
            higher-level code to handle critical initialization failures.
    """
    logger.info(f"Initializing HuggingFaceEmbeddings with model: {model_name}")
    try:
        # HuggingFaceEmbeddings from langchain_community will automatically download 
        # the model from the Hugging Face Hub if it's not already cached locally.
        embeddings = HuggingFaceEmbeddings(model_name=model_name)
        logger.info("Embeddings model initialized successfully.")
        return embeddings
    except Exception as e:
        logger.error(f"Failed to initialize embeddings model '{model_name}': {str(e)}", exc_info=True)
        raise

def create_vector_store(
    chunks: List[Document], 
    save_dir: Union[str, Path] = DEFAULT_VECTOR_STORE_DIR
) -> Optional[FAISS]:
    """
    Create a FAISS vector store from document chunks and save it locally.
    
    This function processes the chunked documents, computes their embeddings, 
    builds the FAISS vector index, and stores it in the designated directory.
    
    Args:
        chunks (List[Document]): The list of chunked LangChain Document objects.
        save_dir (Union[str, Path], optional): Directory path where the FAISS index 
            should be saved. Defaults to 'data/vector_store'.
            
    Returns:
        Optional[FAISS]: The instantiated FAISS vector store object, or None if 
            processing failed or no chunks were provided.
            
    Raises:
        None: Internal exceptions during index creation or saving are caught, logged, 
            and handled gracefully by returning None.
    """
    if not chunks:
        logger.warning("No document chunks were provided to create the vector store.")
        return None
        
    save_path = Path(save_dir)
    logger.info(f"Creating vector store from {len(chunks)} document chunks.")
    
    try:
        # Initialize the embedding model
        embeddings_model = get_embeddings_model()
        
        logger.info("Building FAISS vector index... This may take a moment.")
        # FAISS builds the index by mapping the chunks' text using the embeddings model
        vector_store = FAISS.from_documents(chunks, embeddings_model)
        
        logger.info(f"Saving vector store locally to '{save_path}'")
        
        # Ensure the destination directory exists before saving
        save_path.mkdir(parents=True, exist_ok=True)
        
        # LangChain's save_local creates 'index.faiss' and 'index.pkl' inside save_path
        vector_store.save_local(str(save_path))
        
        logger.info("FAISS vector store successfully created and saved.")
        return vector_store
        
    except Exception as e:
        logger.error(
            f"An error occurred while creating or saving the FAISS vector store: {str(e)}", 
            exc_info=True
        )
        return None
