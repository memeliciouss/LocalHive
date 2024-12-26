from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path("",views.index, name="home"),
    path("create/",views.create, name="createEvent")
]