""" Volunteers Views """
from django.shortcuts import render
from .models import Volunteer


def all_volunteers(request):
    """ A view to show all the volunteers. """
    volunteers = Volunteer.objects.all()

    context = {
        'volunteers': volunteers,
    }

    return render(request, "volunteers/volunteers.html", context)
