web: newrelic-admin run-program gunicorn -b "0.0.0.0:$PORT" -w 3 www.wsgi
worker: python manage.py celeryd -E --loglevel=INFO
