import os, json
from xml.dom import minicompat

from celery import Celery
from celery.schedules import crontab
from loguru import logger


app = Celery(
    "tasks",
    broker=os.environ.get("REDIS_URL", "redis://localhost:6379/0"),
    backend="redis",
)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # call train_model('data-set-a') every 60 sec
    sender.add_periodic_task(60.0, train_model.s("data-set-a"), name="add every 60")

    sender.add_periodic_task(120.0, train_model.s("data-set-b"), expires=10)

    sender.add_periodic_task(
        crontab(hour=10, minute=30, day_of_week=2), train_model.s("data-set-c")
    )


@app.task
def train_model(args):
    logger.info(f"training in progress {args}")
