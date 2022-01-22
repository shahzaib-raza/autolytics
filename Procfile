web: gunicorn djangoProject.wsgi --log-file -
heroku ps:scale web=1
web: python manage.py runserver