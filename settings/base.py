"""
Django settings for ciis project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hello world'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    #'suppliers.apps.SuppliersConfig',
    #'infrastructure.apps.InfrastructureConfig',
    'databazeci.apps.DatabazeciConfig',
    'addresses.apps.AddressesConfig',
    'contacts.apps.ContactsConfig',
    'whoiswho.apps.WhoiswhoConfig',
    'suppliers.apps.SuppliersConfig',
    'socekon.apps.SocekonConfig',
    'brownfields.apps.BrownfieldsConfig',
    'circular_economy.apps.CircularEconomyConfig',
    'ai.apps.AiConfig',
    'dotacni_matice.apps.DotacniMaticeConfig',
    #'entrepreneurial_property.apps.EntrepreneurialPropertyConfig',
    'nested_admin',
    'crispy_forms',
    'leaflet',
    'cigeo.apps.CIGeoConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.sites',
    'vtp.apps.VtpConfig',
    'rest_framework',
    'rest_framework_gis',
    'microsoft_auth',
    'django_filters',
    'drf_yasg',
    'django_bootstrap_breadcrumbs',
    'corsheaders',
    #'rest_pandas',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'ciis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # <- add this line
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'microsoft_auth.context_processors.microsoft',
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = [
    'microsoft_auth.backends.MicrosoftAuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend' # if you also want to use Django's authentication
    # I recommend keeping this with at least one database superuser in case of unable to use others
]

WSGI_APPLICATION = 'ciis.wsgi.application'

#SPATIALITE_LIBRARY_PATH = 'mod_spatialite'
SPATIALITE_LIBRARY_PATH = '/usr/lib/x86_64-linux-gnu/mod_spatialite.so'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.spatialite',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    #os.path.join(BASE_DIR, "cigeo/static")
]

MEDIA_ROOT=os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

LEAFLET_CONFIG = {
    'SPATIAL_EXTENT': (12.1, 48.5, 18.7, 51.1),
    'PLUGINS': {
        'forms': {
            'js': [
                '/static/leaflet/leaflet.forms.js',
                '/static/leaflet/leaflet.extras.js',
                '/static/leaflet/draw/leaflet.draw.js'
            ],
            'css': [
                '/static/leaflet/leaflet.css',
                'static/leaflet/draw/leaflet.draw.css']
        }
    }

}

CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL="/"
SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'drf_renderer_xlsx.renderers.XLSXRenderer',
    ],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

SWAGGER_SETTINGS = {
    "exclude_namespaces": ['rest_logout', ],  # List URL namespaces to ignore
    "SUPPORTED_SUBMIT_METHODS": [  # Specify which methods to enable in Swagger UI
        'get',
        'post',
        'put',
        'delete'
    ],
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    },
    'USE_SESSION_AUTH': True,
    'JSON_EDITOR': True,
    'REFETCH_SCHEMA_ON_LOGOUT': True

}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOW_METHODS = [ 'GET', ]
CORS_ORIGIN_ALLOW_ALL = True
