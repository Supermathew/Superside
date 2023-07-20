"""
Django settings for Superside project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
# import django
# django.setup()
from pathlib import Path
import os
import environ
import dj_database_url

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")

# django-insecure-kn_k(!%)tgz9bg_&&1#iv48fxre%*isp*4%^b5&v0j^h=%=p^a

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG")


ALLOWED_HOSTS = ["localhost","127.0.0.1","superside.onrender.com","http://superside.onrender.com","https://superside.onrender.com","https://superside-admin.vercel.app"]


CSRF_TRUSTED_ORIGINS = ["https://superside.onrender.com"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "navigation.apps.NavigationConfig",
    "rest_framework",
    "rest_framework.authtoken",
    "ckeditor",
    "ckeditor_uploader",
    "accounts",
    "drf_yasg",
    "corsheaders",
    # "navigation",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


CORS_ORIGIN_ALLOW_ALL = env.bool("DJANGO_CORS_ORGIN_ALLOW")
CORS_ALLOWED_ORIGINS = [
    "http://superside.onrender.com",
    "https://superside.onrender.com",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
    "http://localhost:3003",
    "https://superside-admin.vercel.app"

    
]

CORS_ALLOW_CREDENTIALS = env.bool("DJANGO_CORS_ALLOW_CREDENTIALS")

ROOT_URLCONF = "Superside.urls"

CKEDITOR_JQUERY_URL ='https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'	
CKEDITOR_UPLOAD_PATH = "uploads/"	
CKEDITOR_IMAGE_BACKEND = "pillow"	

CKEDITOR_CONFIGS = {	
    'default': {	
        "removePlugins": "exportpdf",	
    }	
}


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "Superside.wsgi.application"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = env("DJANGO_EMAILPORT")
EMAIL_HOST_USER = env("DJANGO_EMAILHOST_USER")
EMAIL_HOST_PASSWORD = env("DJANGO_EMAILHOST_PASSWORD")
EMAIL_USE_TLS = env("DJANGO_EMAIL_USE_TLS")

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],

  'DEFAULT_PARSER_CLASSES': (
          'rest_framework.parsers.FormParser',
          'rest_framework.parsers.MultiPartParser',
          'rest_framework.parsers.JSONParser',
   )

}

# DATABASES ={
#     "default": dj_database_url.parse(env("DATABASE_URL"))
# }

DATABASES ={
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'URL': dj_database_url.parse(env("DATABASE_URL")),
        'NAME': env("PGDATABASE"),
        'USER': env("PGUSER"),
        'PASSWORD': env("PGPASSWORD"),
        'HOST': env("PGHOST"),
        'PORT': env("PGPORT"),
    }
}

database_url = os.environ.get("DATABASE_URL")
DATABASES["default"] = dj_database_url.parse(database_url)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles_build','staticfiles')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

# SIMPLE_JWT = {
#     'ROTATE_REFRESH_TOKENS' : True,
# }

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
     'JSON_EDITOR': True, 
  
}


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE")
CSRF_COOKIE_SECURE = env.bool("DJANGO_CSRF_COOKIE_SECURE")

# Security Headers
SECURE_CONTENT_TYPE_NOSNIFF = env.bool("DJANGO_SECURE_CONTENT_TYPE_NOSNIFF")
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS")
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD")
SECURE_HSTS_SECONDS = env("DJANGO_SECURE_HSTS_SECONDS")





AUTH_USER_MODEL = 'auth.User'
