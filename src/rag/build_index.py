import logging
import sys

# Import the existing pipeline tools exactly as defined previously
from src.rag.chunker import split_documents
from src.rag.embeddings import create_vector_store
from src.rag.loader import load_documents

# Configure module-level logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def run_index_builder() -> None:
    """
    Load raw documents, chunk them syntactically, and embed them into FAISS.
    
    This abstracts the multi-step Retrieval-Augmented Generation ingestion 
    layer into a single programmatic executable.
    """
    logger.info("=" * 60)
    logger.info("🚀 Starting RAG Vector Store Ingestion")
    logger.info("=" * 60)

    try:
        # Step 1: Document Loading
        logger.info("[PHASE 1] Loading raw documents from source...")
        documents = load_documents()
        
        if not documents:
            logger.warning("Ingestion halted early: No valid documents found.")
            sys.exit(0)
            
        logger.info(f"✅ Successfully loaded {len(documents)} document(s).")

        # Step 2: Text Splitting
        logger.info("[PHASE 2] Splitting texts via RecursiveCharacterTextSplitter...")
        chunks = split_documents(documents)
        
        if not chunks:
            logger.warning("Ingestion halted early: Failed to produce viable chunks.")
            sys.exit(0)
            
        logger.info(f"✅ Successfully produced {len(chunks)} structural chunks.")

        # Step 3: Vector Embeddings & Storage
        logger.info("[PHASE 3] Generating embeddings and saving FAISS database locally...")
        create_vector_store(chunks)
        
        logger.info("=" * 60)
        logger.info("✅ FAISS Vector store pipeline generated and saved successfully!")
        logger.info("=" * 60)

    except Exception as e:
        logger.error(f"❌ A critical failure disrupted the build process: {str(e)}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    run_index_builder()
