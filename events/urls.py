from django.contrib import admin
from django.urls import path
from events import views

urlpatterns = [
    path("create/",views.create, name="createEvent")
]