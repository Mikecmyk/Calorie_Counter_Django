# calorie_counter_project/settings.py

from pathlib import Path
import os
import dj_database_url # <--- FIX: Added import here

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - suitable for production now!

# SECURITY WARNING: Use environment variable for the secret key!
# It will use your secure key from the Render dashboard.
SECRET_KEY = os.environ.get('SECRET_KEY', 'default-insecure-key')

# --- ENVIRONMENT SETTINGS (For Render) ---
# DEBUG is True locally, False in production (Render)
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['127.0.0.1', '.render.com', 'calorie-counter-django.onrender.com']


# Application definition

INSTALLED_APPS = [
    # Must be first for static file handling in deployment
    'whitenoise.runserver_nostatic',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Your Apps
    'calorie_tracker',
    'widget_tweaks',
    'whitenoise',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Must be second for static handling
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'calorie_counter_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'calorie_counter_project.wsgi.application'


# --- DATABASE CONFIGURATION (Uses dj-database-url) ---

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL'), # Uses the ENV variable from Render
        conn_max_age=600,
    )
}


# Password validation
# ... (standard password validators)

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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --- PRODUCTION SECURITY AND STATIC FILES ---

# Security settings for Render
# These ensure the app serves securely in production
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Static files (CSS, JavaScript, Images)
# Configuration for Whitenoise and Render's static file collection
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'