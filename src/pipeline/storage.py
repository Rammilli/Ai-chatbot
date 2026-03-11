import hashlib
import logging
import sqlite3
from pathlib import Path
from typing import Any, Dict, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

DEFAULT_DB_DIR = Path("data")
DEFAULT_DB_FILE = DEFAULT_DB_DIR / "news_pipeline.db"


def generate_hash(text: str) -> str:
    """
    Generate SHA256 hash for deduplication support.
    """
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def initialize_database(db_path: Path = DEFAULT_DB_FILE) -> None:
    """
    Initialize SQLite database and articles table.
    """
    try:
        db_path.parent.mkdir(parents=True, exist_ok=True)

        with sqlite3.connect(
            str(db_path),
            check_same_thread=False,
        ) as conn:
            cursor = conn.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS articles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    source_name TEXT NOT NULL,
                    source_url TEXT NOT NULL,
                    article_url TEXT UNIQUE NOT NULL,
                    published_date TEXT NOT NULL,
                    collected_date TEXT NOT NULL,
                    author TEXT,
                    raw_text TEXT,
                    clean_text TEXT,
                    parsed_content TEXT,
                    category TEXT NOT NULL,
                    language TEXT,
                    tags TEXT,
                    hash TEXT UNIQUE
                )
                """
            )

            # Backward compatibility for old DBs
            try:
                cursor.execute("ALTER TABLE articles ADD COLUMN tags TEXT")
            except sqlite3.OperationalError:
                pass

            cursor.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_article_url
                ON articles(article_url)
                """
            )

            conn.commit()

    except sqlite3.Error as e:
        logger.error(
            f"Database initialization failed: {str(e)}",
            exc_info=True,
        )
        raise


def insert_article(
    cursor: sqlite3.Cursor,
    article: Dict[str, Any]
) -> bool:
    """
    Insert one article safely.
    """
    try:
        article_hash = generate_hash(
            article.get("clean_text", "")
        )

        cursor.execute(
            """
            INSERT OR IGNORE INTO articles (
                title,
                source_name,
                source_url,
                article_url,
                published_date,
                collected_date,
                author,
                raw_text,
                clean_text,
                parsed_content,
                category,
                language,
                tags,
                hash
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                article.get("title", "Unknown Title"),
                article.get("source_name", "Unknown Source"),
                article.get("source_url", "Unknown URL"),
                article.get("article_url", ""),
                article.get("published_date", ""),
                article.get("collected_date", ""),
                article.get("author", "Unknown"),
                article.get("raw_text", ""),
                article.get("clean_text", ""),
                article.get("parsed_content", ""),
                article.get("category", "uncategorized"),
                article.get("language", "en"),
                article.get("tags", ""),
                article_hash,
            ),
        )

        return cursor.rowcount > 0

    except sqlite3.Error as e:
        logger.warning(
            f"Insert failed for {article.get('article_url')}: {str(e)}"
        )
        return False


def store_articles(
    articles: List[Dict[str, Any]],
    db_path: Path = DEFAULT_DB_FILE,
) -> int:
    """
    Store classified articles into SQLite database.
    """
    if not articles:
        logger.warning("No articles to store")
        return 0

    initialize_database(db_path)

    inserted_count = 0

    try:
        with sqlite3.connect(
            str(db_path),
            check_same_thread=False,
        ) as conn:
            cursor = conn.cursor()

            for article in articles:
                if not article.get("article_url"):
                    continue

                if insert_article(cursor, article):
                    inserted_count += 1

            conn.commit()

        logger.info(
            f"{inserted_count} new articles inserted"
        )

        return inserted_count

    except sqlite3.Error as e:
        logger.error(
            f"Storage transaction failed: {str(e)}",
            exc_info=True,
        )
        return inserted_count


if __name__ == "__main__":
    print("=" * 70)
    print("🚀 AI News Data Pipeline - Storage Test")
    print("=" * 70)

    mock_articles = [
        {
            "title": "Sample News",
            "source_name": "BBC",
            "source_url": "http://bbc.com",
            "article_url": "http://bbc.com/sample-news",
            "published_date": "2024-01-01",
            "collected_date": "2024-01-01",
            "author": "Unknown",
            "raw_text": "Sample raw content",
            "clean_text": "Sample clean content",
            "parsed_content": "Sample clean content",
            "category": "technology",
            "language": "en",
            "tags": "mock, tag, AI",
        }
    ]

    inserted = store_articles(mock_articles)

    print(f"\nInserted rows: {inserted}")
    print("\n" + "=" * 70)