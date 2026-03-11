import logging
from pathlib import Path
from typing import List, Union

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    UnstructuredMarkdownLoader,
)
from langchain_core.documents import Document

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Default path for document storage
DEFAULT_DATA_DIR = Path("data/documents")


def load_documents(data_dir: Union[str, Path] = DEFAULT_DATA_DIR) -> List[Document]:
    """
    Load and extract text from supported document types in the specified directory.

    Supported file types:
    - PDF (.pdf)
    - Text (.txt)
    - Markdown (.md)

    Returns:
        List[Document]: Combined LangChain documents.
    """

    base_path = Path(data_dir)
    combined_documents: List[Document] = []

    if not base_path.exists():
        logger.warning(f"The directory '{base_path}' does not exist. No documents loaded.")
        return combined_documents

    if not base_path.is_dir():
        logger.error(f"The path '{base_path}' is not a valid directory.")
        return combined_documents

    loaders_mapping = {
        ".pdf": PyPDFLoader,
        ".txt": TextLoader,
        ".md": UnstructuredMarkdownLoader,
    }

    logger.info(f"Scanning directory '{base_path}' for compatible documents.")

    for file_path in base_path.iterdir():

        if not file_path.is_file():
            continue

        file_extension = file_path.suffix.lower()

        if file_extension not in loaders_mapping:
            logger.debug(f"Ignoring unsupported file type: {file_path.name}")
            continue

        loader_class = loaders_mapping[file_extension]

        try:
            if file_extension == ".txt":
                loader = loader_class(str(file_path), encoding="utf-8")
            else:
                loader = loader_class(str(file_path))

            documents = loader.load()
            combined_documents.extend(documents)

            logger.info(f"Loaded {file_extension}: {file_path.name}")

        except Exception as e:
            logger.error(
                f"Failed to load document '{file_path.name}'. Error: {str(e)}",
                exc_info=True,
            )

    logger.info(
        f"Document loading complete. Extracted a total of "
        f"{len(combined_documents)} LangChain document objects."
    )

    return combined_documents