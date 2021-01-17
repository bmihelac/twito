import os
from logging.config import dictConfig

DMI_TCAT_USERNAME = os.getenv('DMI_TCAT_USERNAME')
DMI_TCAT_PASSWORD = os.getenv('DMI_TCAT_PASSWORD')

CACHE_CONFIG = {
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 30 * 24 * 60 * 60,  # 30 days
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.getenv('DB_URL', 'twito.sqlite3'),
    }
}

USE_TZ=True

INSTALLED_APPS = (
    'tweets',
)

CELERY_CONFIG = {
    'BROKER_URL': os.getenv('REDIS_URL', 'redis://redis'),
    'RESULT_BACKEND': os.getenv('REDIS_URL', 'redis://redis'),
}

SECRET_KEY = os.getenv('SECRET_KEY', 'THIS_SHOULD_BE_SECRET')

# set logging configuration
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})
