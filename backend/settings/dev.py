from .base import *

DEBUG = True

#  ALLOWED_HOSTS = ["*"]
#Better (safer even in dev)
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

#  Why?    "*" allows any host header (not a good habit).   This builds production mindset

# ==============================
# DATABASE
# ==============================
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


"""
#Deploying to production , Large data, Real client project
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # or sqlite3
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
"""