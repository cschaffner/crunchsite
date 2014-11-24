web: newrelic-admin run-program waitress-serve --port=$PORT www.wsgi:application
worker: python manage.py celeryd -E --loglevel=INFO
