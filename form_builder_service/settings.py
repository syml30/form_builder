from pathlib import Path
import logging
import dotenv
import os

dotenv.load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',

    'rest_framework',
    'drf_yasg',

    'form_builders.apps.FormBuildersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'form_builder_service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'form_builder_service.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
if os.environ.get('DEPLOY') == 'True':
    DATABASES = {
        'default': {
            'ENGINE': os.environ.get('DATABASES_ENGINE'),
            'NAME': os.environ.get('DATABASES_NAME'),
            'USER': os.environ.get('DATABASES_USER'),
            'PASSWORD': os.environ.get('DATABASES_PASSWORD'),
            'HOST': os.environ.get('DATABASES_HOST'),
            'PORT': os.environ.get('DATABASES_PORT'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


STATIC_URL = '/form_builder_static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'form_builder_files')

# Media files (Images, Videos, Voices, Documents)

MEDIA_URL = '/form_builder_media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'form_builder_uploads')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOWED_ORIGINS = []
CROS_ALLOW_CREDENTIALS = True




IMAGE_UPLOADER_SERVER = os.environ.get('IMAGE_UPLOADER_SERVER')
IMAGE_UPLOADER_ADDRESS = f"{IMAGE_UPLOADER_SERVER}/{os.environ.get('IMAGE_UPLOADER_ADDRESS')}"
IMAGE_UPLOADER_API_KEY = os.environ.get('IMAGE_UPLOADER_API_KEY')

DOCUMENT_UPLOADER_SERVER = os.environ.get('DOCUMENT_UPLOADER_SERVER')
DOCUMENT_UPLOADER_ADDRESS = f"{DOCUMENT_UPLOADER_SERVER}/{os.environ.get('DOCUMENT_UPLOADER_ADDRESS')}"
DOCUMENT_UPLOADER_API_KEY = os.environ.get('DOCUMENT_UPLOADER_API_KEY')

# Logger config
logging.basicConfig(
    level=logging.DEBUG,
    # filename='.log',
    filemode='w',
    format='log: %(levelname)s - %(asctime)s - module: %(module)s - line number: %(lineno)d  - message: '
           '\"%(message)s\" '
)
