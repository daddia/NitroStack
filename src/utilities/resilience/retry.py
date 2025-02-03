from tenacity import retry, stop_after_attempt, wait_exponential, RetryError
import logging

logger = logging.getLogger(__name__)

def retry_on_failure(max_attempts=3, wait_seconds=2):
    return retry(
        stop=stop_after_attempt(max_attempts),
        wait=wait_exponential(multiplier=1, min=wait_seconds, max=10),
        reraise=True
    )

@retry_on_failure()
def sample_task():
    # Example task that may fail and trigger retries
    logger.info("Attempting task...")
    raise ValueError("Simulated failure")
