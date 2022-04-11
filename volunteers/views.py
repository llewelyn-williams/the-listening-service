""" Volunteers Views """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Volunteer
from .forms import VolunteerForm


def all_volunteers(request):
    """ A view to show all the volunteers. """
    volunteers = Volunteer.objects.all()

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("Cannot search with a blank search term."))
                return redirect(reverse('volunteers'))

            queries = Q(forename__icontains=query) | Q(surname__icontains=query) | Q(description__icontains=query)
            volunteers = volunteers.filter(queries)

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


def add_volunteer(request):
    """ Add a volunteer """
    form = VolunteerForm()
    template = 'volunteers/add_volunteer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
