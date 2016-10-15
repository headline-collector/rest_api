"""
Django settings for info_tracker project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6g_=s8il8c8a3d^c#rpi5cn!prn+a$)9clz#p)74c1_qh!$7(u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework', # include session & basic authentication
    'api',
    'corsheaders',
    'third_party',
    'rest_framework_httpsignature', # sign auth
    'rest_framework.authtoken' # token authentication; header must includes 'Authorizaiton Token: xx' or 'WWWW-Authorizaiton: Token'
                                # should only be available in 'https'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # added CORS middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'info_tracker.urls'

WSGI_APPLICATION = 'info_tracker.wsgi.application'

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'/api/.*$'

# CORS_ORIGIN_WHITELIST = ('localhost', )
# CORS_ORIGIN_REGEX_WHITELIST = (
#     # "^(https?://)?127.0.0.1:8000", "^(https?://)?127.0.0.1:8001",
#     CORS_URLS_REGEX,
# )

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CONFIG = {
    'local_test':{
        'ENGINE': 'mysql.connector.django',#'django.db.backends.sqlite3',
        'NAME':  'info_tracker',
        'USER': 'root',#'cpc_analysis',#'root',
        'PASSWORD': '020139',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {'charset': 'utf8mb4'}
    }

}

DATABASES = {
    'default': CONFIG['local_test'],
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ( os.path.join(BASE_DIR, "static") ),

)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        # 'api.auth.authentication.SignatureAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'EXCEPTION_HANDLER': 'api.auth.exceptions.sys_exc_handler',
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
        'api.throttling.AnonRateThrottlePerMin',
        'api.throttling.UserRateThrottlePerMin',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon/min': '600/min',
        'anon': '1000/day',
        'user/min': '6000/min',
        'user': '100000/day',
    },
}


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

# authentication_backends

# DATETIME FORMAT
DATETIME_INPUT_FORMATS = ['%Y-%m-%d','']

# Default Auth User
AUTH_USER_MODEL = 'api.App'
# Default Authentication Backends
AUTHENTICATION_BACKENDS = ('api.auth.backends.QueryBackend',)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': u"%(asctime)s [%(levelname)s]:%(filename)s, %(name)s, in line %(lineno)s >> \n%(message)s".encode('utf-8'),
            'datefmt': "%a, %d, %b, %Y %H:%M:%S",#"%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': u'[%(levelname)s] %(filename)s %(lineno)s: %(message)s'.encode('utf-8')
        },
        'classic_formatter':{
            'format': u"%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s >>  %(message)s".encode('utf-8'),
            'datefmt' : "%a, %d, %b, %Y %H:%M:%S",
        },
        'default': {
            'format': u"%(asctime)s [%(levelname)s] [%(name)s:%(lineno)s] >> %(message)s".encode('utf-8'),
            'datefmt': "%d/%b/%Y %H:%M:%S",
        }
    },
    'handlers': {
        'console':{
            'level':'INFO',
            'class':'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose'
        },
        'email_info_tracer':{
            'level': 'ERROR',
            'class': 'logging.handlers.SMTPHandler',
            'formatter': 'verbose',
            'mailhost': '',
            'fromaddr': 'info_tracker_notify@weiboyi.com',
            'toaddrs': '',
            'subject': 'Info tracker API ERROR !',
            'credentials': ('', '')
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': 'sys.log'
        }
    },
    'loggers': {
        'django': {
            'handlers':['console', 'file',],
            'propagate': True,
            'level':'INFO',
        },
        'api.model':{
            'handlers':['console', ],
            'propagate': True,
            'level':'INFO',
        },
        'api.router':{
            'handlers': ['console'],
            'propagate': True,
            'level':'INFO'
        },
        'api.tests':{
            'handlers': ['console'],
            'propagate': True,
            'level':'INFO',

        },
        'third_party.tests':{
            'handlers': ['console'],
            'propagate': True,
            'level': 'INFO',
        },
    }
}