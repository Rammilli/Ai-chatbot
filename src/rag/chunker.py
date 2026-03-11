import logging
from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

logger = logging.getLogger(__name__)

DEFAULT_CHUNK_SIZE = 1000
DEFAULT_CHUNK_OVERLAP = 200

def split_documents(
    documents: List[Document],
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    chunk_overlap: int = DEFAULT_CHUNK_OVERLAP
) -> List[Document]:
    """
    Split a list of LangChain Document objects into smaller chunks using 
    RecursiveCharacterTextSplitter.
    
    This function processes the loaded documents, preserving their original 
    metadata while splitting the text content into manageable chunks suitable 
    for embeddings generation.
    
    Args:
        documents (List[Document]): The input list of parsed LangChain Document objects.
        chunk_size (int, optional): The maximum size of each text chunk. Defaults to 1000.
        chunk_overlap (int, optional): The overlap size between consecutive chunks 
            to maintain context. Defaults to 200.
            
    Returns:
        List[Document]: A new list containing the chunked LangChain Document objects.
        
    Raises:
        None: Exceptions are caught and logged, returning an empty list upon failure.
    """
    if not documents:
        logger.warning("No documents provided for chunking. Returning an empty list.")
        return []

    logger.info(
        f"Initializing RecursiveCharacterTextSplitter with chunk_size={chunk_size} "
        f"and chunk_overlap={chunk_overlap}."
    )
    
    try:
        # LangChain's RecursiveCharacterTextSplitter is recommended for standard text
        # as it tries to keep paragraphs, sentences, and words together in that order.
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            # Enabling add_start_index preserves the position of the chunk in the original text
            # inside the metadata, which is highly useful for context retrieval.
            add_start_index=True 
        )
        
        logger.info(f"Starting to chunk {len(documents)} document(s)...")
        
        # split_documents automatically preserves the original document's metadata
        chunked_documents = text_splitter.split_documents(documents)
        
        logger.info(
            f"Successfully split {len(documents)} document(s) into "
            f"{len(chunked_documents)} chunk(s)."
        )
        
        return chunked_documents
        
    except Exception as e:
        logger.error(
            f"An error occurred while splitting documents: {str(e)}", 
            exc_info=True
        )
        # Returning an empty list ensures the pipeline doesn't crash catastrophically,
        # but the error is logged for upstream monitoring.
        return []
