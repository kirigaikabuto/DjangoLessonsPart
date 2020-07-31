from django import forms
from .models import *


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        fields = ('phone_number', 'abo'
                                  ''
                                  'ut', 'photo', 'city', 'hobby')