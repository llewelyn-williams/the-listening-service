""" Volunteer Models """
from django.db import models


class Volunteer(models.Model):
    """ Volunteer Listener Model """
    forename = models.CharField(max_length=254)
    surname = models.CharField(max_length=254)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.forename} {self.surname}'
