# -*- coding: utf-8 -*-

import os
DEBUG = True
TEMPLATE_DEBUG = DEBUG

BASE_DIR = os.path.dirname(__file__)

ADMINS = (
    ('Matías Iturburu', 'maturburu@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'potaje.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Argentina/Cordoba'

LANGUAGE_CODE = 'es-AR'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = 'http://localhost/potaje/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = '93st-g$)00b@r4mcovx=tln#p+t&s6xf8-2tby44jp(s&5&cle'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'potaje.urls'

TEMPLATE_DIRS = (
    'templates'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.markup',
    'potaje'
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
