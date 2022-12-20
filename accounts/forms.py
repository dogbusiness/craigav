from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    birth_date = forms.DateField()
    phone_number = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "birth_date", 'phone_number', 'city', 'country']

class ChangeUserForm(forms.ModelForm):
    birth_date = forms.DateField()
    phone_number = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ["username", "email", "birth_date", 'phone_number', 'city', 'country']

    # method for prepopulating fields with current logged in user
    def prepopulate(user_profile):
        initial_in_fields = {"username": user_profile.username, "email": user_profile.email, 
        "birth_date": user_profile.profile.birth_date, 'phone_number': user_profile.profile.phone_number, 
        'city': user_profile.profile.city, 'country': user_profile.profile.country}
        return initial_in_fields
    
    # неудачное попытка переписания сохранения. Приводит к созданию пользователя без пароля)
    # def save(self, change_form, commit=True):
    #     # calling for method in default django ModelForm to save user
    #     user = super(ChangeUserForm, self).save()
    #     user.refresh_from_db()
    #     user.profile.birth_date = change_form.cleaned_data.get('birth_date')
    #     user.profile.phone_number = change_form.cleaned_data.get('phone_number')
    #     user.profile.city = change_form.cleaned_data.get('city')
    #     user.profile.country= change_form.cleaned_data.get('country')
    #     user.save()
    #     return user




