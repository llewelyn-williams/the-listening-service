from django.shortcuts import (render, reverse, redirect,
                              get_object_or_404, HttpResponse)
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

from .forms import ReviewForm
from .models import Review

from profiles.models import UserProfile
from profiles.forms import UserProfileForm


@login_required
def add_review(request):

    if request.method == "POST":
        form_data = {
            'review_text': request.POST['review_text'],
        }
        review_form = ReviewForm(form_data)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.save()
            messages.success(request, 'Review added successfully.')

            return redirect(
                reverse()
                )
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
