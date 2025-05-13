from .base import *



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w!3ykdec*tmyg*_a$j7n#jk6duqmrbs&58d5&casqp6a%eg+-8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

STATIC_URL = "static/"

STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/' 

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

