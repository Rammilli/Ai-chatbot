import logging
import time

import schedule

from .classifier import classify_articles
from .collector import collect_news
from .dedup import remove_duplicates
from .parser import parse_articles
from .storage import store_articles

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)

SCHEDULE_INTERVAL_MINUTES = 30


def run_pipeline() -> None:
    """
    Execute full news pipeline once.
    """
    logger.info("=" * 60)
    logger.info("🚀 Starting full pipeline run")
    logger.info("=" * 60)

    try:
        # Phase 1: Collect
        raw_articles = collect_news()
        logger.info(f"Collected: {len(raw_articles)} articles")

        if not raw_articles:
            logger.warning("No articles collected")
            return

        # Phase 2: Parse
        parsed_articles = parse_articles(raw_articles)
        logger.info(f"Parsed: {len(parsed_articles)} articles")

        if not parsed_articles:
            logger.warning("No parsed articles")
            return

        # Phase 3: Classify
        classified_articles = classify_articles(parsed_articles)
        logger.info(f"Classified: {len(classified_articles)} articles")

        if not classified_articles:
            logger.warning("No classified articles")
            return

        # Phase 4: Deduplicate
        deduped_articles = remove_duplicates(classified_articles)
        logger.info(f"Deduplicated: {len(deduped_articles)} articles")

        if not deduped_articles:
            logger.warning("No articles after deduplication")
            return

        # Phase 5: Store
        inserted_rows = store_articles(deduped_articles)
        logger.info(f"Stored: {inserted_rows} new rows")

        logger.info("✅ Pipeline completed successfully")

    except Exception as e:
        logger.error(
            f"Pipeline failed: {str(e)}",
            exc_info=True,
        )

    logger.info("=" * 60)


def start_scheduler() -> None:
    """
    Start recurring scheduler.
    """
    logger.info("Starting scheduler service")

    # Immediate first run
    run_pipeline()

    # Schedule repeated execution
    schedule.every(SCHEDULE_INTERVAL_MINUTES).minutes.do(run_pipeline)

    logger.info(
        f"Scheduler active: every {SCHEDULE_INTERVAL_MINUTES} minutes"
    )

    try:
        while True:
            schedule.run_pending()
            time.sleep(10)

    except KeyboardInterrupt:
        logger.info("🛑 Scheduler stopped by user")


if __name__ == "__main__":
    start_scheduler()