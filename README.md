windmillwindupsite
==================

Install from scratch on Mac OSX:
* install homebrew
* install virtualenv and virtualenvwrapper
* get source code from GitHub:
git clone git@github.com:lkleuver/windmillwindupsite.git
* create a local_settings.py file from sample_local_settings.py in the www subfolder
(or get the configuration file from Les or Chris)

1. create virtualenv by
~/ > mkvirtualenv crunchsite

2. add the following line
export DJANGO_SETTINGS_MODULE=www.settings
to the file 'postactivate' in the ~HOME/Envs/crunchsite/bin/ (or wherever your virtualenvs are stored)

This will automatically set the environmental variable DJANGO_SETTINGS_MODULE to the right value.

3. in the project home:
python manage.py syncdb --all
When asked, create a superuser

4. python manage.py migrate --fake

5. python manage.py runserver


Push master branch to heroku:
1. git push heroku master


Run a local postgres server:
* install Postgresql:
~ >brew install postgresql
~ >mkdir ~/Postgresql
~ >pg_ctl init ~/Postgresql

start the server:
~ > pg_ctl start -D ~/Postgresql/ -l ~/Postgresql/logfile


to pull the heroku database to the localhost (using the database wwsite)
~/Sites/windmillwindupsite > heroku pg:pull DATABASE_URL wwsite

* Daily backups of the HEROKU database are now kept on Amazon S3 (via another heroku app)

to push the local db to heroku, we first need to totally empty the heroku db:
(be careful! Pushing should never be necessary)
~ >heroku pg:reset HEROKU_POSTGRESQL_GRAY_URL
~ >heroku pg:push wwsite HEROKU_POSTGRESQL_GRAY_URL

to restore a dump locally:
~ >pg_restore --verbose --clean --no-acl -d wwsite DUMPFILE.dump

to restore a backup from pgbackups on heroku:
https://devcenter.heroku.com/articles/pgbackups#restoring-from-backup
the command will be something like the following:
heroku pgbackups:restore HEROKU_POSTGRESQL_BLACK b251

to reset team, registration and pickup data (or run other sql scripts):
http://stackoverflow.com/questions/15237366/how-to-execute-a-sql-script-on-heroku
$ cat reset_all_team_data.sql | heroku pg:psql --app windmillwindupsite

locally:
$ psql -h localhost -d wwsite -f sqlscripts/reset_all_team_data.sql

