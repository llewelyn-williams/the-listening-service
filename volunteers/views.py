""" Volunteers Views """
from django.shortcuts import (render, redirect, reverse,
                              get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from reviews.models import Review
from reviews.forms import ReviewForm
from profiles.models import UserProfile

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

            queries = (
                Q(forename__icontains=query) |
                Q(surname__icontains=query) |
                Q(description__icontains=query)
                )
            volunteers = volunteers.filter(queries)

    context = {
        'volunteers': volunteers,
    }

    return render(request, "volunteers/volunteers.html", context)


def volunteer_detail(request, volunteer_id):
    """ Show an individual volunteer. """
    volunteer = get_object_or_404(Volunteer, pk=volunteer_id)
    review_form = ReviewForm()
    reviews = Review.objects.filter(volunteer=volunteer)
    approved_reviews = Review.objects.filter(
        volunteer=volunteer,
        approved=True)
    context = {
        'volunteer': volunteer,
        'review_form': review_form,
        'reviews': reviews,
        'approved_reviews': approved_reviews,
    }

    return render(request, "volunteers/volunteer_detail.html", context)


@login_required
def add_volunteer(request):
    """ Add a volunteer """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = VolunteerForm(request.POST, request.FILES)
        if form.is_valid():
            volunteer = form.save()
            messages.success(
                request,
                f'Successfully added volunteer: \
                    {volunteer.forename} {volunteer.surname}')
            return redirect(reverse('volunteer_detail', args=[volunteer.id]))
        else:
            messages.error(
                request,
                'Failed to add volunteer. Please ensure the form is valid.')
    else:
        form = VolunteerForm()

    template = 'volunteers/add_volunteer.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_volunteer(request, volunteer_id):
    """ Edit a volunteer """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('home'))

    volunteer = get_object_or_404(Volunteer, pk=volunteer_id)
    if request.method == 'POST':
        form = VolunteerForm(request.POST, request.FILES, instance=volunteer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated volunteer!')
            return redirect(reverse('volunteer_detail', args=[volunteer.id]))
        else:
            messages.error(
                request,
                'Failed to update volunteer. Please ensure the form is valid.')
    else:
        form = VolunteerForm(instance=volunteer)
        messages.info(
            request, (
                f'You are editing {volunteer.forename} {volunteer.surname}'
                )
            )

    template = 'volunteers/edit_volunteer.html'
    context = {
        'form': form,
        'volunteer': volunteer,
    }

    return render(request, template, context)


@login_required
def delete_volunteer(request, volunteer_id):
    """ Delete a volunteer """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('home'))

    volunteer = get_object_or_404(Volunteer, pk=volunteer_id)

    volunteer.delete()
    messages.success(request, 'Volunteer record removed!')

    return redirect(reverse('volunteers'))


@login_required
def add_review(request, volunteer_id):

    if request.method == "POST":
        form_data = {
            'review_text': request.POST['review_text'],
        }
        review_form = ReviewForm(form_data)
        if review_form.is_valid():

            volunteer = get_object_or_404(Volunteer, pk=volunteer_id)
            profile = UserProfile.objects.get(user=request.user)

            review = review_form.save(commit=False)
            # Attach the user's profile to the order
            review.user_profile = profile
            review.volunteer = volunteer

            review.save()
            messages.success(request, 'Review submitted successfully.')
            return redirect(reverse('volunteer_detail', args=[volunteer.id]))

        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
