""" Volunteers URLs """
from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_volunteers, name="volunteers")
]
