""" This is a sample file of the local settings for setting up the windmillwindup development server

For the development server to work, you must create your own local_settings.py file in this directory
and then fill in each of these fields with the information relevant to your setup.

get the correct keys etc. either from Heroku by running: heroku config
or directly from Les or Chris

this one is for local development of Christian Schaffner
"""

import os.path
import sys

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''


DEBUG = False

if DEBUG:
    USE_STATICFILES = False # If True, you need to re-generate the static files after every change
                            # or else you will be viewing the old ones
else:
    USE_STATICFILES = True

TWITTER_OAUTH_TOKEN = ''
TWITTER_OAUTH_SECRET = ''
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''

FLICKR_API_KEY = ''
FLICKR_API_SECRET = ''

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
