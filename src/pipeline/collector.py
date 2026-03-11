import logging
from datetime import datetime, timezone
from typing import Any, Dict, List, Set, Optional

import feedparser
import requests
from requests.exceptions import RequestException

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# Request timeout configuration
REQUEST_TIMEOUT = 10

# RSS feed sources
DEFAULT_SOURCES = [
    {
        "name": "BBC News",
        "url": "http://feeds.bbci.co.uk/news/rss.xml",
    },
    {
        "name": "TechCrunch",
        "url": "https://techcrunch.com/feed/",
    },
    {
        "name": "The Hindu",
        "url": "https://www.thehindu.com/news/national/feeder/default.rss",
    },
]


def fetch_feed_content(url: str, timeout: int = REQUEST_TIMEOUT) -> Optional[bytes]:
    """
    Fetch raw RSS feed content safely.
    """
    try:
        response = requests.get(
            url,
            timeout=timeout,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        response.raise_for_status()
        return response.content

    except RequestException as e:
        logger.error(f"Network error while fetching feed '{url}': {str(e)}")
        return None

    except Exception as e:
        logger.error(
            f"Unexpected error while fetching feed '{url}': {str(e)}",
            exc_info=True,
        )
        return None


def process_feed_source(
    source: Dict[str, str],
    seen_urls: Set[str]
) -> List[Dict[str, Any]]:
    """
    Process one RSS source and return normalized articles.
    """
    source_name = source.get("name", "Unknown Source")
    source_url = source.get("url", "")

    if not source_url:
        logger.warning(f"No URL found for source '{source_name}'")
        return []

    logger.info(f"Fetching RSS feed from {source_name}: {source_url}")

    raw_content = fetch_feed_content(source_url)

    if not raw_content:
        logger.warning(f"Failed to fetch content from '{source_name}'")
        return []

    parsed_feed = feedparser.parse(raw_content)

    if getattr(parsed_feed, "bozo", False):
        logger.warning(
            f"Feed parsing warning for '{source_name}': {parsed_feed.bozo_exception}"
        )

    articles: List[Dict[str, Any]] = []
    current_collection_date = datetime.now(timezone.utc).isoformat()

    for entry in parsed_feed.entries[:10]:
        article_url = entry.get("link", "").strip()

        if not article_url or article_url in seen_urls:
            continue

        seen_urls.add(article_url)

        published_date = entry.get(
            "published",
            entry.get("updated", current_collection_date)
        )

        article = {
            "title": entry.get("title", "Unknown Title").strip(),
            "source_name": source_name,
            "source_url": source_url,
            "article_url": article_url,
            "published_date": published_date,
            "collected_date": current_collection_date,
        }

        articles.append(article)

    logger.info(
        f"{source_name}: {len(articles)} unique articles collected"
    )

    return articles


def collect_news(
    sources: Optional[List[Dict[str, str]]] = None
) -> List[Dict[str, Any]]:
    """
    Collect articles from all configured RSS feeds.
    """
    if sources is None:
        sources = DEFAULT_SOURCES

    logger.info(f"Starting collection from {len(sources)} sources")

    master_article_list: List[Dict[str, Any]] = []
    seen_urls: Set[str] = set()

    for source in sources:
        try:
            articles = process_feed_source(source, seen_urls)
            master_article_list.extend(articles)

        except Exception as e:
            logger.error(
                f"Error processing source '{source.get('name')}': {str(e)}",
                exc_info=True,
            )

    logger.info(
        f"Collection complete: {len(master_article_list)} total articles"
    )

    return master_article_list


if __name__ == "__main__":
    print("=" * 70)
    print("🚀 Initializing AI News Data Pipeline")
    print("Layer 1: Collector Module")
    print("=" * 70)

    try:
        collected_articles = collect_news()

        if collected_articles:
            print(
                f"\n✅ Successfully collected {len(collected_articles)} articles\n"
            )

            for i, article in enumerate(collected_articles[:2], start=1):
                print(f"\n--- Article {i} ---")
                for key, value in article.items():
                    print(f"{key}: {value}")

            if len(collected_articles) > 2:
                print(f"\n... and {len(collected_articles) - 2} more articles")

        else:
            print("\n⚠️ No articles collected")

    except Exception as e:
        print(f"\n❌ Collector failed: {str(e)}")
        logger.error(str(e), exc_info=True)

    print("\n" + "=" * 70)