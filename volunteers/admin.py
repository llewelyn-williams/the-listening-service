from django.contrib import admin
from .models import Volunteer

class VolunteerAdmin(admin.ModelAdmin):
    list_display = (
        'forename',
        'surname',
        'image',
    )

# Register your models here.
admin.site.register(Volunteer, VolunteerAdmin)
