from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    birth_date = forms.DateField()
    phone_number = forms.CharField(max_length=100, help_text='Phone Number')
    city = forms.CharField(max_length=100, help_text='City')
    country = forms.CharField(max_length=100, help_text='Country')

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "birth_date", 'phone_number', 'city', 'country']