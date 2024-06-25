from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
""" from .models import FormaPago """

class CustomUserCreationForm(UserCreationForm):
    pass

""" class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = "__all__" """