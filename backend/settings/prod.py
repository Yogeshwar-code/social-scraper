from .base import *
import os
import dj_database_url

DEBUG = False

# ALLOWED_HOSTS = ["yourdomain.com"]   # before for local machine

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    os.environ.get("RENDER_EXTERNAL_HOSTNAME"),
]

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),
        'USER': os.getenv("DB_USER"),
        'PASSWORD': os.getenv("DB_PASSWORD"),
        'HOST': os.getenv("DB_HOST"),
        'PORT': os.getenv("DB_PORT"),
    }
}
"""

DATABASES = {
    'default': dj_database_url.parse(
        os.getenv("DATABASE_URL"),
        conn_max_age=600
    )
}


#   HTTPS & Security (production only)
# ==============================
# SECURITY SETTINGS (PRODUCTION)       and  Only True in production otherwise it should be false
# ==============================
                                           # This means:
SECURE_SSL_REDIRECT = True              #Force HTTPS
CSRF_COOKIE_SECURE = True               #Cookies only over HTTPS
SESSION_COOKIE_SECURE = True            #Protect against session hijacking
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')