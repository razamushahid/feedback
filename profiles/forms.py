# from django.forms import forms
from django import forms


class ProfileForm(forms.Form):
    user_image = forms.ImageField()
