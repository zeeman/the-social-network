from django import forms

from .models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'about', 'profile_visibility']
        widgets = {
            'profile_visibility': forms.RadioSelect,
        }
