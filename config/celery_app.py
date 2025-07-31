from celery import Celery
import os
import warnings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # Replace with your project name

# Attempt to import Django
try:
    import django
    # Check if Django is installed correctly
    if django.VERSION < (1, 11):
        raise ImportError('Celery 5.x requires Django 1.11 or later.')
except ImportError as e:
    warnings.warn(f"Django is not installed or the version is incompatible: {e}")
    raise  # Re-raise the exception to stop execution if Django is not available
except Exception as e:
    warnings.warn(f"An error occurred while checking Django: {e}")
    raise  # Re-raise the exception for any other errors

# Create a new Celery application instance
app = Celery('your_project_name')  # Replace with your project name

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()








