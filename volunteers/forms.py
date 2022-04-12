from django import forms
from .widgets import CustomClearableFileInput
from .models import Volunteer


class VolunteerForm(forms.ModelForm):

    class Meta:
        model = Volunteer
        fields = ('forename', 'surname', 'description', 'image')

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput)
