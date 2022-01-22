from django.contrib import admin
from django.urls import path
from . import views

app_name = 'testApp'
urlpatterns = [
    path('', views.model_name, name="index"),
    path('', views.appView, name="Home page"),
]
