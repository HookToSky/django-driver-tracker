import os
from celery import Celery
from django.conf import settings
from datetime import timedelta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'driverTracker.settings')

app = Celery('driverTracker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


app.conf.beat_schedule = {
     'update_driver_locations': {
        'task': 'update_driver_locations', 
        'schedule': timedelta(seconds = 5.0),
        'args': (),
    }
}