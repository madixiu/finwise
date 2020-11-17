"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.conf import settings as django_settings
from datetime import timedelta
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#o&r+pyx=x(a^g!xxs6ntqls5dtad8y%q95sfcgekm-h7(6*+f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

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
    'channels',
    'rest_framework',
    'api',
    'websocket',
    "graphene_django",
    "graphql_jwt.refresh_token.apps.RefreshTokenConfig",
    "graphql_auth",
    "django_filters",
    "users"

    
    # 'subscriptions',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# graphQL
AUTH_USER_MODEL = 'users.CustomUser'

GRAPHENE = {
    'SCHEMA': 'backend.schema.schema', # this file doesn't exist yet
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}

AUTHENTICATION_BACKENDS = [
    # 'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
    'graphql_auth.backends.GraphQLAuthBackend',

]

GRAPHQL_JWT = {
    "JWT_VERIFY_EXPIRATION": True,
    "JWT_ALLOW_ANY_CLASSES": [
        "graphql_auth.mutations.Register",
        "graphql_auth.mutations.VerifyAccount",
        "graphql_auth.mutations.ResendActivationEmail",
        "graphql_auth.mutations.SendPasswordResetEmail",
        "graphql_auth.mutations.PasswordReset",
        "graphql_auth.mutations.ObtainJSONWebToken",
        "graphql_auth.mutations.VerifyToken",
        "graphql_auth.mutations.RefreshToken",
        "graphql_auth.mutations.RevokeToken",
        "graphql_auth.mutations.VerifySecondaryEmail",
    ],
    # optional for long running refresh token
    "JWT_LONG_RUNNING_REFRESH_TOKEN": True,
    'JWT_EXPIRATION_DELTA': timedelta(minutes=11),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=1),
}

# graphql options
GRAPHQL_AUTH = {
    "LOGIN_ALLOWED_FIELDS": ['email', 'phone_number'],
    "REGISTER_MUTATION_FIELDS" : ["email", "username" ,"first_name" , "last_name" , "phone_number"],
    "REGISTER_MUTATION_FIELDS_OPTIONAL": ["age","gender","degree"],
    "UPDATE_MUTATION_FIELDS": ["email","age","gender","password","username","degree"],
    "ALLOW_LOGIN_NOT_VERIFIED": False,
    "ALLOW_LOGIN_WITH_SECONDARY_EMAIL": False,
    "EXPIRATION_ACTIVATION_TOKEN": timedelta(days=1),
    "EXPIRATION_PASSWORD_RESET_TOKEN": timedelta(hours=1),
    # email stuff
    "EMAIL_FROM": getattr(django_settings, "DEFAULT_FROM_EMAIL", "mr.robotc7@gmail.com"),
    "SEND_ACTIVATION_EMAIL": True,
    "EMAIL_SUBJECT_ACTIVATION": "email/activation_subject.txt",
    "EMAIL_SUBJECT_ACTIVATION_RESEND": "email/activation_subject.txt",
    "EMAIL_SUBJECT_SECONDARY_EMAIL_ACTIVATION": "email/activation_subject.txt",
    "EMAIL_SUBJECT_PASSWORD_RESET": "email/password_reset_subject.txt",
    # email templates
    "EMAIL_TEMPLATE_ACTIVATION": "email/activation_email.html",
    "EMAIL_TEMPLATE_ACTIVATION_RESEND": "email/activation_email.html",
    "EMAIL_TEMPLATE_SECONDARY_EMAIL_ACTIVATION": "email/activation_email.html",
    "EMAIL_TEMPLATE_PASSWORD_RESET": "email/password_reset_email.html",
    # ...
}
# --- EMAIL
#console email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# gmail smtp
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mr.robotc7@gmail.com'
#Must generate specific password for your app in [gmail settings][1]
EMAIL_HOST_PASSWORD = 'yamahdi001'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# graphQL end


ROOT_URLCONF = 'backend.urls'
ASGI_APPLICATION = "backend.routing.application"

# added this to prevent @took too long to shutdown then killed it@ problem
ASGI_THREADS = 1000

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase.db',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#       # 'HOST': 'db',                   # noqa
#         'HOST': 'localhost',
#         'PORT': 5432,

#     }

# }

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # noqa
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

# Authentication 





CORS_ORIGIN_ALLOW_ALL = True

# Celery Configuration

CELERY_BROKER_URL = 'redis://redis:6379'
CELERY_RESULT_BACKEND = 'redis://redis:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'


# addons ----------------------------- # noqa
REDIS_URL = 'redis://localhost:6379/1'

CHANNEL_LAYERS = {
  
}
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             # "hosts": [os.environ['REDIS_URL']],
#             # "hosts": ["redis://127.0.0.1:6379"],
#             "hosts": [("127.0.0.1", 6379)],
#         },
#     },
# }


# CSRF TOKEN SETTING
# CSRF_COOKIE_NAME = "csrftoken"
CSRF_COOKIE_NAME = "XSRF-TOKEN"

# django redis cache TEST...............................................
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        #"LOCATION": os.environ['REDIS_URL'],  # Here we have Redis DSN (for ex. redis://localhost:6379/1) # noqa
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "MAX_ENTRIES": 1000  # Increase max cache entries to 1k (from 300)
        },
    }
}


UNICODE_JSON = True