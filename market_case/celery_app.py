import os

from celery import Celery

from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'market.settings')

app = Celery('market', broker='redis://localhost')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.conf.task_serializer = 'json'
app.conf.result_backend = 'rpc://'
app.autodiscover_tasks()
