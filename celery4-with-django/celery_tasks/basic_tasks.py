import os, json

import requests
from celery import Celery
from loguru import logger


app = Celery(
    "tasks",
    broker=os.environ.get("REDIS_URL", "redis://localhost:6379/0"),
    backend="redis",
)


@app.task
def latest_bitcoin_price(currency_code: str = None) -> object:
    """
    CoinDesk Bitcoin Price Index (XBP) api fetches bitcoin prices that represents
    an average of bitcoin prices across leading global exchanges
    :type currency_code: str
    :param currency_code: coinDesk supported currency
    :return: json object
    """

    if (
        currency_code
        and isinstance(currency_code, str)
        and currency_code.upper() in ["USD", "GBP", "EUR", "CNY"]
    ):
        bpi_url = (
            f"https://api.coindesk.com/v1/bpi/currentprice/{currency_code.upper()}.json"
        )
    else:
        bpi_url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    response = requests.get(bpi_url)

    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        logger.error(f"failed get 200 response from {bpi_url}")
        return None
