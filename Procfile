web: newrelic-admin run-program gunicorn www.wsgi -b "0.0.0.0:$PORT" -w 3
worker: python manage.py celeryd -E --loglevel=INFO
