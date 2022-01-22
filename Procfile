web: gunicorn pakwheels-analytics-app.wsgi:application --log-file -
heroku ps:scale web=1
web: python manage.py runserver