# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from config.celery_app import app as celery_app  # Update to the new filename

__all__ = ('celery_app',)

