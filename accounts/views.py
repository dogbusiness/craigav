from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

# Create your views here.
def user_login(request):
    pass

def user_register(request):
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save()
            user.refresh_from_db()
            user.profile.birth_date = reg_form.cleaned_data.get('birth_date')
            user.profile.phone_number = reg_form.cleaned_data.get('phone_number')
            user.profile.city = reg_form.cleaned_data.get('city')
            user.profile.country= reg_form.cleaned_data.get('country')
            user.save()
            username = reg_form.cleaned_data.get('username')
            password = reg_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # нужен редирект на страницу профиля
            return redirect('')

    else:
        reg_form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': reg_form})