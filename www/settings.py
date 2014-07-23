# -*- coding: utf-8 -*-
import os

gettext = lambda s: s
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

# check if we are on heroku (production) or on local development
ON_HEROKU = True
if 'ON_HEROKU' in os.environ:
    ON_HEROKU = True
    DEBUG = os.environ.get('DEBUG', False) # if DEBUG exists on Heroku, use DEBUG mode, otherwise not
    SITE_ID = 1 # crunchsite.herokuapp.com
else:
    DEBUG = True
    SITE_ID = 1 # crunchsite.herokuapp.com
    # SITE_ID = 2 # 127.0.0.1:8000


ADMINS = (
    ('Christian Schaffner', 'huebli@gmail.com'),
    ('Les Kleuver', 'les.kleuver@gmail.com'),
)

MANAGERS = ADMINS
SEND_BROKEN_LINK_EMAILS = False
CELERY_SEND_TASK_ERROR_EMAILS = True



TEMPLATE_DEBUG = DEBUG

DATETIME_FORMAT = 'l, j E Y, G:i'
DATE_FORMAT = 'l, j E Y'



# Parse database configuration from $DATABASE_URL (required for Heroku)
# or use database.sqlite as default
import dj_database_url
# now changed to local postgres server
# run it with: pg_ctl start -D ~/Postgresql/ -l ~/Postgresql/logfile
# then run: heroku pg:pull HEROKU_POSTGRESQL_GRAY_URL wwsite
# to pull the heroku database to the localhost (using the database wwsite)
DATABASES = {'default': dj_database_url.config(default='postgres://localhost:5432/crunchsite')}


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'


# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

DATETIME_FORMAT = 'l, j E Y, G:i'
DATE_FORMAT = 'l, j E Y'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, "www/static"),
    os.path.join(PROJECT_PATH, 'www/bower_components'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'pipeline.finders.PipelineFinder',
)


MEDIA_ROOT = os.path.join(PROJECT_PATH, "media")
MEDIA_URL = "/media/"

STATIC_ROOT = 'staticfiles'
#os.path.join(PROJECT_PATH, "static")
STATIC_URL = "/static/"
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

COUNTRIES_FLAG_URL = 'flags/{code}.png'

BASE_URL = u'http://crunchsite.herokuapp.com'

if not ON_HEROKU:
    BASE_URL = 'http://127.0.0.1:8000'

# if on Heroku, use Amazon S3 for static files:
if ON_HEROKU:
    # Amazon S3 credentials
    AWS_ACCESS_KEY_ID       = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY   = os.environ['AWS_SECRET_ACCESS_KEY']

    SECRET_KEY = os.environ['SECRET_KEY']

# Amazon S3 URL
AWS_HEADERS = {
    "Cache-Control": "public, max-age=86400",
}
AWS_STORAGE_BUCKET_NAME = 'crunchweb'
S3_URL = 'https://s3-eu-west-1.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME

DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
DEFAULT_S3_PATH = "media"
MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_URL = '//s3-eu-west-1.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME

# maybe we have to change this to False at some point
AWS_S3_SECURE_URLS = False
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False
AWS_REDUCED_REDUNDANCY = False
AWS_IS_GZIPPED = False



# disabling serving static files from S3 for now, until
# TODO: js issues are resolved
#STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
#STATIC_S3_PATH = "static"
#STATIC_ROOT = "/%s/" % STATIC_S3_PATH
#STATIC_URL = '//s3-eu-west-1.amazonaws.com/%s/static/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


ALLOWED_HOSTS = ['127.0.0.1', 'crunchsite.herokuapp.com', 'crunch-ultimate.net', 'localhost']


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings',
    'sekizai.context_processors.sekizai',
    # 'zinnia.context_processors.version',
    # Required by allauth template tags
    "django.core.context_processors.request",
    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    # "django.contrib.auth.backends.ModelBackend",
    'member.auth.MyModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    # 'reversion.middleware.RevisionMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

if ON_HEROKU:
    os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS', '').replace(',', ';')
    os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
    os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')

    CACHES = {
      'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',
        'TIMEOUT': 500,
        'BINARY': True,
        'OPTIONS': {
            'tcp_nodelay': True,
            'remove_failed': 4
        }
      },
        'staticfiles': {
            "BACKEND": "django_pylibmc.memcached.PyLibMCCache",
            "TIMEOUT": 60 * 60 * 24 * 365,
            'BINARY': True,
            'OPTIONS': {
                'tcp_nodelay': True,
                'remove_failed': 4
            }
        }

    }
else:
    # disable caches for development
    CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }

    # # or turn it on for testing
    # CACHES = {
    # 'default': {
    #     'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    #     'LOCATION': 'unique-snowflake',
    #     }
    # }

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 0
CACHE_MIDDLEWARE_KEY_PREFIX = ''

CMS_CACHE_DURATIONS = {'content': 60}

# ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
LOGIN_REDIRECT_URL = 'member:my_detail'
SOCIALACCOUNT_QUERY_EMAIL = True
# SOCIALACCOUNT_PROVIDERS = \
#     {'facebook':
#        {'SCOPE': ['email', 'publish_stream'],
#         'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
#         'METHOD': 'oauth2',
#         'LOCALE_FUNC': 'path.to.callable',
#         'VERIFIED_EMAIL': False}}


ROOT_URLCONF = 'www.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'www.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, "templates"),
)

LANGUAGES = [
    ('en', 'English'),
]

CMS_TEMPLATES = (
    ('default_section.html', 'Default section'),
    ('home.html', 'HOME'),
    ('faq.html', 'FAQ'),
    ('subsubmenu.html', 'Extra menu'),
    ('thumbgrid.html', "Grid"),
    ('global_placeholders.html', 'Global Placeholders'),
    ('message.html', 'Plain message'),
    ('section_no_sidebar.html', 'CMS section without side bar'),
    ('page.html', 'testing CMS'),
)
CMS_PERMISSION = True


EMAIL_CONFIRMATION_DAYS = 100
EMAIL_BCC = 'huebli@gmail.com' # will be used as BCC address in all emails sent
DEFAULT_FROM_EMAIL = 'webmaster@crunch-ultimate.net'
SERVER_EMAIL = 'Crunch Site <webmaster@crunch-ultimate.net>'
EMAIL_TEST = False
EMAIL_TEST_RECIPIENT = ['huebli@gmail.com']

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

if not ON_HEROKU:
    EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
    EMAIL_FILE_PATH = '{0}/app-messages'.format(PROJECT_PATH)
#    EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
elif ON_HEROKU:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
    EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']

#    EMAIL_FILE_PATH = 'app-messages/' # change this to a proper location

USE_CELERY = True
#### Celery stuff
if USE_CELERY:
    CELERYD_CONCURRENCY = 1
    CELERYD_NODES="w1"
    CELERY_RESULT_BACKEND="amqp"
    BROKER_POOL_LIMIT = 1
    if ON_HEROKU:
        BROKER_URL = os.environ['CLOUDAMQP_URL']
else:
    # Uncomment these lines to turn off celery and make everything run inline
    BROKER_HOST = ""
    BROKER_PORT = 0
    BROKER_USER = ""
    BROKER_PASSWORD = ""
    BROKER_VHOST = ""
    BROKER_BACKEND='memory'
    CELERY_ALWAYS_EAGER = True


INSTALLED_APPS = (
    'autocomplete_light',
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'pipeline',
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'reversion',
    'www',
    'djcelery',
    's3_folder_storage',
    'gunicorn',
    'filer',
    'easy_thumbnails',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    # 'cmsplugin_contact',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'bootstrapform',
    'member',
    'team',
    'localflavor',
    'import_export',
    # 'customplugins',
    # 'zinnia',
    # 'cmsplugin_zinnia',
    # 'django.contrib.markup',
    # 'django_extensions',
    # 'team',
    # 'openscreen',
    # 'volunteer',
    # 'twitter_tag',
    # 'cmsplugin_flickr',
    # 'cmsplugin_vimeo',
    # 'form_designer',
    # 'form_designer.contrib.cms_plugins.form_designer_form',
    # 'cmsplugin_contact',
    # 'adminsortable',
    # 'captcha',
    # 'prediction',
    # 'sortedm2m',
    # 'groupme',
)

THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

#ZINNIA (BLOG) SETTINGS
ZINNIA_AUTO_CLOSE_COMMENTS_AFTER = 0
#never got this to work, a pity.
#ZINNIA_ENTRY_BASE_MODEL = 'cmsplugin_zinnia.placeholder.EntryPlaceholder'


RECAPTCHA_PUBLIC_KEY = '6Lclf-wSAAAAABiYzvnSKXBjOKf1ENPA4B5h5ZnC'
RECAPTCHA_PRIVATE_KEY = '6Lclf-wSAAAAAKUfTJwkd_LhotOQ7tLYtFs5-WZx'

CAPTCHA_FONT_SIZE = 40
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'

GROUPME_HOST = 'https://api.groupme.com/v3'
GROUPME_TEST_BOT_ID = 'f87002597e8edc2d835585e3ff'
GROUPME_TESTING = False   # sends all messages to the GroupMe group with id GROUPME_TEST_BOT_ID instead of to the real receivers

LEAGUEVINE_HOST = "https://api.leaguevine.com"
LEAGUEVINE_TOKEN_URL = "https://www.leaguevine.com"
# LEAGUEVINE_HOST = "http://api.localhost:8000"
# LEAGUEVINE_TOKEN_URL = "http://localhost:8000"


if ON_HEROKU:
    #TWITTER
    # get them by running  'heroku config' and put those env variables locally in local_settings.py!
    TWITTER_OAUTH_TOKEN = os.environ['TWITTER_OAUTH_TOKEN']
    TWITTER_OAUTH_SECRET = os.environ['TWITTER_OAUTH_SECRET']
    TWITTER_CONSUMER_KEY = os.environ['TWITTER_CONSUMER_KEY']
    TWITTER_CONSUMER_SECRET = os.environ['TWITTER_CONSUMER_SECRET']

    #flickr
    FLICKR_API_KEY = os.environ['FLICKR_API_KEY']
    FLICKR_API_SECRET = os.environ['FLICKR_API_SECRET']

    # # leaguevine
    # LEAGUEVINE_CLIENT_ID = os.environ['LEAGUEVINE_CLIENT_ID']
    # LEAGUEVINE_CLIENT_PWD = os.environ['LEAGUEVINE_CLIENT_PWD']
    #
    # # groupme
    # GROUPME_TOKEN = os.environ['GROUPME_TOKEN']



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                       'pathname=%(pathname)s lineno=%(lineno)s ' +
                       'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            "level": "INFO",
            "class": "logging.StreamHandler",
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        "django": {
            "handlers": ["console"],
            "level": 'INFO',
        },
        "testlog": {
            "handlers": ["console"],
            "level": 'DEBUG',
        },
        "django.db.backends": {
            "handlers": ["console"],
            'level': 'DEBUG',
        }

    }
}

PIPELINE_YUGLIFY_BINARY = os.path.abspath(os.path.dirname(__file__) + '/../node_modules/yuglify/bin/yuglify')
PIPELINE_LESS_BINARY = os.path.abspath(os.path.dirname(__file__) + '/../node_modules/less/bin/lessc')
PIPELINE_COMPILERS = (
  'pipeline.compilers.less.LessCompiler',
)

PIPELINE_CSS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'
PIPELINE_JS_COMPRESSOR = 'pipeline.compressors.yuglify.YuglifyCompressor'


PIPELINE_CSS = {
    'core': {
        'source_filenames': (
          'bootstrap/less/bootstrap.less',
        ),
        'output_filename': 'css/core.css',
    },
}

PIPELINE_JS = {
    'core': {
        'source_filenames': (
          'bootstrap/dist/js/bootstrap.js',
          'jquery/dist/jquery.js',
        ),
        'output_filename': 'js/core.js',
    }
}


# use local_settings when available
try:
    from local_settings import *
except ImportError:
    pass