import logging
import sys

# Import the core ingestion modules
from src.rag.chunker import split_documents
from src.rag.embeddings import create_vector_store
from src.rag.loader import load_documents

# Configure logging at the INFO level so we can see the exact steps executing
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

def main():
    """
    Main entry point for testing the full RAG ingestion pipeline.
    
    This script orchestrates the loading of source documents, splits them into 
    manageable text chunks, and then computes their embeddings to be saved into 
    your local FAISS vector store database.
    
    It serves as a clean utility to populate your vector database prior to 
    querying it with ask.py.
    """
    print("\n🚀 Starting the RAG Document Ingestion Pipeline...\n")
    print("-" * 50)
    
    try:
        # Step 1: Load documents from the configured data directory
        logger.info("[Step 1/3] Loading source documents...")
        documents = load_documents()
        
        if not documents:
            logger.warning(
                "No documents were loaded. Ensure there are valid .pdf or .txt "
                "files inside the 'data/documents' directory before running."
            )
            sys.exit(0)
            
        print(f"✅ Loading complete. Loaded {len(documents)} document(s).")
        print("-" * 50)
        
        # Step 2: Split the full documents into chunks
        logger.info("[Step 2/3] Chunking documents into smaller pieces...")
        chunks = split_documents(documents)
        
        if not chunks:
            logger.error("Failed to split documents into chunks.")
            sys.exit(1)
            
        print(f"✅ Chunking complete. Created {len(chunks)} text chunk(s).")
        print("-" * 50)
        
        # Step 3: Compute embeddings and save the FAISS vector store locally
        logger.info("[Step 3/3] Generating embeddings and building FAISS index...")
        logger.info("This process may take a while depending on paragraph counts.")
        vector_store = create_vector_store(chunks)
        
        if not vector_store:
            logger.error(
                "Failed to generate embeddings and save the local vector store. "
                "View logs for the specific stack trace."
            )
            sys.exit(1)
            
        print("✅ Vector store created and saved successfully to data/vector_store!")
        print("-" * 50)
        
        print("\n🎉 Pipeline execution completed successfully. "
              "Your RAG database is ready for queries!\n")
        
    except Exception as e:
        logger.error(f"\nAn unhandled error occurred during ingestion testing: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
