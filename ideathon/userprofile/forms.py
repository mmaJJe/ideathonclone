from django import forms
from . models import rectify_profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = rectify_profile
        fields = ['name', 'email', 'school', 'contact','introduce' ]

