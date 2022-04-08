""" Volunteers Views """
from django.shortcuts import render, get_object_or_404
from .models import Volunteer


def all_volunteers(request):
    """ A view to show all the volunteers. """
    volunteers = Volunteer.objects.all()

    context = {
        'volunteers': volunteers,
    }

    return render(request, "volunteers/volunteers.html", context)


def volunteer_detail(request, volunteer_id):
    """ Show an individual volunteer. """
    volunteer = get_object_or_404(Volunteer, pk=volunteer_id)

    context = {
        'volunteer': volunteer,
    }

    return render(request, "volunteers/volunteer_detail.html", context)
