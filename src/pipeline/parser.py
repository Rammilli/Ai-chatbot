import logging
import re
from typing import Any, Dict, List, Optional

from newspaper import Article
from newspaper.article import ArticleException

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


def clean_text(text: str) -> str:
    """
    Clean extracted article text.
    """
    if not text:
        return ""

    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def extract_article_content(url: str) -> Optional[str]:
    """
    Extract main article text from URL.
    """
    if not url:
        return None

    try:
        article = Article(
            url,
            fetch_images=False,
            keep_article_html=False,
        )

        article.download()
        article.parse()

        if not article.text.strip():
            logger.warning(f"No article text extracted from: {url}")
            return None

        return clean_text(article.text)

    except ArticleException as e:
        logger.error(f"Article extraction failed for '{url}': {str(e)}")
        return None

    except Exception as e:
        logger.error(
            f"Unexpected parsing error for '{url}': {str(e)}",
            exc_info=True,
        )
        return None


def parse_articles(
    articles: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Parse collected articles and enrich with parsed_content.
    """
    logger.info(f"Starting parser for {len(articles)} articles")

    enriched_articles: List[Dict[str, Any]] = []

    for index, article in enumerate(articles, start=1):
        article_url = article.get("article_url")
        title = article.get("title", "Unknown Title")
        source_name = article.get("source_name", "Unknown Source")

        logger.info(
            f"[{index}/{len(articles)}] Parsing {source_name}: {title}"
        )

        if not article_url:
            logger.warning(f"Skipping article without URL: {title}")
            continue

        parsed_content = extract_article_content(article_url)

        if parsed_content:
            enriched_article = article.copy()
            enriched_article["parsed_content"] = parsed_content
            enriched_articles.append(enriched_article)

        else:
            logger.warning(
                f"Skipping article due to failed extraction: {article_url}"
            )

    logger.info(
        f"Parser complete: {len(enriched_articles)} successfully enriched"
    )

    return enriched_articles


if __name__ == "__main__":
    print("=" * 70)
    print("🚀 AI News Data Pipeline - Parser Test")
    print("=" * 70)

    mock_articles = [
        {
            "title": "Sample Article",
            "source_name": "TechCrunch",
            "source_url": "https://techcrunch.com/feed/",
            "article_url": "https://techcrunch.com/",
            "published_date": "2024-01-01",
            "collected_date": "2024-01-01",
        }
    ]

    parsed = parse_articles(mock_articles)

    print(f"\nParsed articles: {len(parsed)}")

    if parsed:
        print("\nPreview:")
        for key, value in parsed[0].items():
            if key == "parsed_content":
                print(f"{key}: {value[:200]}...")
            else:
                print(f"{key}: {value}")

    print("\n" + "=" * 70)