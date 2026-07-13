import os

from celery import Celery

# Set the default Django settings module
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings.development",
)

app = Celery("nk_ai")

# Read Celery settings from Django settings
app.config_from_object(
    "django.conf:settings",
    namespace="CELERY",
)

# Auto-discover tasks.py from installed apps
app.autodiscover_tasks()