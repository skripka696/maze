
from __future__ import absolute_import

from celery import shared_task
import actions


@only_one( timeout=60 * 5)
@shared_task
def run_spider():
    actions.run_spider()

