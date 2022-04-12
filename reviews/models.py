from django.db import models
from profiles.models import UserProfile
from volunteers.models import Volunteer


class Review(models.Model):
    """ Review Model """
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='reviews')
    volunteer = models.ForeignKey(
        Volunteer,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='volunteers')
    review_text = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
