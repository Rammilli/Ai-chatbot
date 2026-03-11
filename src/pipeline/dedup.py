import logging
from typing import Any, Dict, List, Set

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


def remove_duplicates(
    articles: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Remove duplicate articles while preserving order.
    """
    if not articles:
        logger.warning("No articles received for deduplication")
        return []

    logger.info(f"Deduplicating {len(articles)} articles")

    unique_articles: List[Dict[str, Any]] = []

    seen_urls: Set[str] = set()
    seen_titles: Set[str] = set()

    dropped_count = 0

    for article in articles:
        raw_url = article.get("article_url")
        raw_title = article.get("title")

        url = raw_url.strip().lower() if isinstance(raw_url, str) else ""
        title = raw_title.strip().lower() if isinstance(raw_title, str) else ""

        if not url and not title:
            dropped_count += 1
            continue

        if url:
            if url in seen_urls:
                dropped_count += 1
                continue

            if title and title in seen_titles:
                dropped_count += 1
                continue

            seen_urls.add(url)

            if title:
                seen_titles.add(title)

            unique_articles.append(article)

        elif title:
            if title in seen_titles:
                dropped_count += 1
                continue

            seen_titles.add(title)
            unique_articles.append(article)

    logger.info(
        f"Dedup complete: kept {len(unique_articles)}, dropped {dropped_count}"
    )

    return unique_articles


if __name__ == "__main__":
    print("=" * 70)
    print("🚀 Dedup Test")
    print("=" * 70)

    sample = [
        {
            "title": "OpenAI Launches Model",
            "article_url": "https://site.com/a"
        },
        {
            "title": "openai launches model",
            "article_url": "https://site.com/b"
        }
    ]

    result = remove_duplicates(sample)

    print(f"Remaining: {len(result)}")
    print("=" * 70)