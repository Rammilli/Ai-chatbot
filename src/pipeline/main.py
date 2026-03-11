import logging

from .scheduler import run_pipeline

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


def main():
    """
    Entry point for one full AI News Pipeline execution.
    """
    print("\n🚀 Starting AI News Data Pipeline...\n")

    try:
        run_pipeline()
        print("\n✅ Pipeline execution completed successfully.\n")

    except Exception as e:
        logger.error(
            f"Pipeline execution failed: {str(e)}",
            exc_info=True,
        )


if __name__ == "__main__":
    main()