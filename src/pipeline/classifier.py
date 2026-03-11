import logging
from typing import Any, Dict, List, Optional

from transformers import pipeline

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

TARGET_CATEGORIES = [
    "politics",
    "technology",
    "sports",
    "business",
    "entertainment",
]

classifier_pipeline: Optional[object] = None


def load_classifier():
    """
    Load zero-shot classifier once.
    """
    global classifier_pipeline

    if classifier_pipeline is None:
        try:
            logger.info("Loading zero-shot classifier model...")
            classifier_pipeline = pipeline(
                "zero-shot-classification",
                model="facebook/bart-large-mnli",
                device=-1,
            )
            logger.info("Classifier loaded successfully.")

        except Exception as e:
            logger.error(
                f"Failed to load classifier: {str(e)}",
                exc_info=True,
            )
            classifier_pipeline = None


def get_dominant_category(text: str) -> str:
    """
    Predict dominant category.
    """
    load_classifier()

    if classifier_pipeline is None:
        return "uncategorized"

    inference_text = text[:1500]

    try:
        result = classifier_pipeline(
            inference_text,
            TARGET_CATEGORIES,
            truncation=True,
        )

        return result["labels"][0]

    except Exception as e:
        logger.error(
            f"Classification failed: {str(e)}"
        )
        return "uncategorized"


def classify_articles(
    articles: List[Dict[str, Any]]
) -> List[Dict[str, Any]]:
    """
    Add category to parsed articles.
    """
    if not articles:
        logger.warning("No articles received for classification")
        return []

    logger.info(f"Classifying {len(articles)} articles")

    classified_articles: List[Dict[str, Any]] = []

    for index, article in enumerate(articles, start=1):
        title = article.get("title", "Unknown Title")
        content = article.get("clean_text", "")

        logger.info(f"[{index}/{len(articles)}] {title}")

        if not content.strip():
            category = "uncategorized"
        else:
            category = get_dominant_category(content)

        enriched_article = article.copy()
        enriched_article["category"] = category

        classified_articles.append(enriched_article)

    logger.info("Classification complete")

    return classified_articles


if __name__ == "__main__":
    print("=" * 70)
    print("🚀 AI News Data Pipeline - Classifier Test")
    print("=" * 70)

    mock_articles = [
        {
            "title": "OpenAI launches new model",
            "parsed_content": (
                "OpenAI introduced a new artificial intelligence model "
                "for enterprise applications."
            ),
        }
    ]

    results = classify_articles(mock_articles)

    for item in results:
        print(f"\nTitle: {item['title']}")
        print(f"Category: {item['category']}")

    print("\n" + "=" * 70)