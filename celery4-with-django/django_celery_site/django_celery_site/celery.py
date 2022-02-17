from __future__ import absolute_import

import os

from celery import Celery

project_name = "django_celery_site"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{project_name}.settings")

app = Celery(project_name)

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print("request: {0!r}".format(self.request))
