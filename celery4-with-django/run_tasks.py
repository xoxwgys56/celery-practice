import time, sys
from loguru import logger

from celery_tasks.tasks import latest_bitcoin_price

if __name__ == "__main__":
    result = latest_bitcoin_price.delay("usd")

    logger.info(f"Task finished? {result.ready()}")
    logger.info(f"Task result: {result.result}")

    time.sleep(10)

    logger.info(f"Task finished? {result.ready()}")
    logger.info(f"Task result: {result.result}")
