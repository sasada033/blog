from .settings_common import *


# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False


# Static files (CSS, JavaScript, Images)

STATIC_ROOT = '/usr/share/nginx/html/static'

MEDIA_ROOT = '/usr/share/nginx/html/media'


# Amazon SES settings

AWS_SES_ACCESS_KEY_ID = env('AWS_SES_ACCESS_KEY_ID')

AWS_SES_SECRET_ACCESS_KEY = env('AWS_SES_SECRET_ACCESS_KEY')

EMAIL_BACKEND = 'django_ses.SESBackend'

SERVER_EMAIL = env('SERVER_EMAIL')


# Log settings

LOGGING = {
    'version': 1,  # fixed 1
    'disable_existing_loggers': False,

    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'post': {
            'handlers': ['file'],
            'level': 'INFO',
        },
    },

    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'prod',
            'when': 'D',
            'interval': 1,
            'backupCount': 7,
        },
    },

    'formatters': {
        'prod': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}


# security settings

# security.W004
SECURE_HSTS_SECONDS = 31536000

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# security.W006
SECURE_CONTENT_TYPE_NOSNIFF = True

# security.W007
SECURE_BROWSER_XSS_FILTER = True

# security.W008
SECURE_SSL_REDIRECT = True

# security.W012
SESSION_COOKIE_SECURE = True

# security.W016
CSRF_COOKIE_SECURE = True

# security.W019
X_FRAME_OPTIONS = 'DENY'

# security.W021
SECURE_HSTS_PRELOAD = True

# security.W022
SECURE_REFERRER_POLICY = 'no-referrer-when-downgrade'
