""" Volunteers URLs """
from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_volunteers, name="volunteers"),
    path("<int:volunteer_id>/", views.volunteer_detail,
         name="volunteer_detail"),
    path('add/', views.add_volunteer, name='add_volunteer'),
    path('edit/<int:volunteer_id>/', views.edit_volunteer,
         name='edit_volunteer'),
    path('delete/<int:volunteer_id>/', views.delete_volunteer,
         name='delete_volunteer'),
    path('add_review/<int:volunteer_id>/',
         views.add_review, name='add_review'),
]
