from __future__ import absolute_import, unicode_literals
import json

from celery import Task
import requests
from loguru import logger

from .celery import app


@app.task()
def latest_bitcoin_price(currency_code: str = None) -> object:
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
