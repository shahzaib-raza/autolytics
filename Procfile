web: gunicorn djangoProject.wsgi:application --log-file -
heroku ps:scale web=1
web: python manage.py runserver