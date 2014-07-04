% web: newrelic-admin run-program gunicorn -b "0.0.0.0:$PORT" -w 3 www.wsgi
%web: gunicorn www.wsgi
web: waitress-serve --port=$PORT www.wsgi:application
%worker: python manage.py celeryd -E --loglevel=INFO
