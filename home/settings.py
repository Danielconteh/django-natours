"""
Django settings for home project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from cgi import test
from pathlib import Path
import os
import django_heroku 


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5nq@1e8v+#iw6mtj21^b8lw60t&%9@-upt6s70ef&^zgc5k()^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['django-natours.herokuapp.com']
# ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 
    'cloudinary_storage',
    'cloudinary',
    
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Login via Google as an exemple, you can choose facebook, twitter as you like
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    
    'tour',    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'home.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'home.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3'
       
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

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "/static/")

# where django should watch for static files
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# gathering static files in a single directory so it can easy be serve
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# media storage location
MEDIA_ROOT = BASE_DIR / 'uploads'

# the media root to start serving...
MEDIA_URL = '/Django_Natours/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [

    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'APP': {
            'client_id': '1045610393790-67euil14f1nc9acfdcn38i86lo9toegf.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        },
     
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
         
    },
     'github': {
        'APP': {
            'client_id': 'b57051e7c7982b2db3a2',
            'secret': '02d5168f3406c7e50d2afdbb7e4b8f424e6af14f',
            'key':''
        }
    }
}

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True


ACCOUNT_LOGOUT_REDIRECT_URL='/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'


ACCOUNT_EMAIL_VERIFICATION = 'none'
# ACCOUNT_EMAIL_VERIFICATION = "optional"



# STRIPE

STRIPE_SECRET_KEY='sk_test_51I9BgDIWgSTi3yR4wmHgwYFRtV3WC6YLhZCPv4rzd9tYo8APmusDjfo8eZc7U0PjU2SynSBJYrXQ8Rwm5G3Wntd200RtLZzPdL'
STRIPE_WEBHOOK_SECRET_KEY='whsec_qkCIsGEtsIBUyq6wKv9yOyCoYX8uFO39'
# 'whsec_4f1aef745add61f41d720a6f3dbeb715a2b2d7c76bfede6d074a3d53dfb547e2'
#whsec_qkCIsGEtsIBUyq6wKv9yOyCoYX8uFO39




# CLOUDINARY CONFIGURATION



CLOUDINARY_STORAGE = {
    'CLOUD_NAME':'dbmrdwsfb',
    'API_KEY':'857545946179366',
    'API_SECRET':'xqg9bflE9TuBBxEwlGbAekJtycI'
}


# Then all the way at the bottom of the file
# ... 
django_heroku.settings(locals())