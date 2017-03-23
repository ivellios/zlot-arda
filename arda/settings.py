# -*- coding: utf-8 -*-
# Django settings for arda project.

import os,sys

PROJECT_ROOT = os.path.abspath(os.path.split(__file__)[0])
sys.path.append(os.path.join(PROJECT_ROOT, '../apps'))


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Ivellios', 'ivellios@arda.org.pl')
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'arda.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


#DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#DATABASE_NAME = 'kamienski_arda'             # Or path to database file if using sqlite3.
#DATABASE_USER = 'kamienski'             # Not used with sqlite3.
#DATABASE_PASSWORD = 'adax4100'         # Not used with sqlite3.
#DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Warsaw'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pl'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
import os.path
MEDIA_ROOT = os.path.join(os.path.dirname(__file__),'../public/site_media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/site_media/'


#STATICFILES_DIRS = (
#    os.path.join(PROJECT_ROOT, 'site_media'),
#)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATIC_ROOT = os.path.join(PROJECT_ROOT, '../public/static_media')
STATIC_URL = '/static_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static_media/admin/'


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    #'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.filesystem.Loader',
    #'django.template.loaders.app_directories.load_template_source',
    'django.template.loaders.app_directories.Loader'
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)




ROOT_URLCONF = 'arda.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'zapisy',
    'mailing',
    'news',
    'galeria',
    'static',
    'zlot',
    'south',
    'patroni',
    'thumbnails',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    'arda.context.site',
)

LOGIN_URL='/konto/logowanie/'

AUTH_PROFILE_MODULE = "zapisy.Uczestnik"



#AUTHENTICATION_BACKENDS = (
#    'zpaisy.auth_backends.UczestnikModelBackend',
#)

CUSTOM_USER_MODEL = 'zapisy.Uczestnik'
ZAPISY_OTWARTE = True
LOGIN_REDIRECT_URL = '/'

#Email settings
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_PASSWORD = 'neverset'
#EMAIL_HOST_USER = 'no-reply@arda.org.pl'
#EMAIL_PORT = 587
#EMAIL_SUBJECT_PREFIX = '[Zlot Arda] '
#EMAIL_USE_TLS = True
#SERVER_EMAIL = 'no-reply@arda.org.pl'
#DEFAULT_FROM_EMAIL = 'no-reply@arda.org.pl'
#
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ALLOWED_HOSTS = ['arda.org.pl', 'www.arda.org.pl', ]


try:
    from settings_local import *
except ImportError:
    pass
