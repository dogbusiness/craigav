from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, ChangeUserForm, SetPasswordForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User # temp import need to relocate to form new save method

#---------- Auth Stuff ----------#
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # нужен редирект на страницу профиля
            return redirect('/')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        form = AuthenticationForm(request)
    return render(request, 'accounts/login.html', {'form': form})

def user_logout(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    logout(request)
    return redirect('/')

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
            return redirect('/')

    else:
        if request.user.is_authenticated:
            return redirect('/')
        reg_form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': reg_form})

def change_profile(request):
    if request.method == 'POST':
        change_form = ChangeUserForm(request.POST)
        if change_form.is_valid():
            # get user from db in order to change him
            user = User.objects.get(id=request.user.id)
            user.username = change_form.cleaned_data.get('username')
            user.email = change_form.cleaned_data.get('email')
            user.save()
            user.refresh_from_db()
            user.profile.birth_date = change_form.cleaned_data.get('birth_date')
            user.profile.phone_number = change_form.cleaned_data.get('phone_number')
            user.profile.city = change_form.cleaned_data.get('city')
            user.profile.country= change_form.cleaned_data.get('country')
            user.save()
            user.refresh_from_db()
            # relogin in case username changed
            user = authenticate(username=user.username, password=user.password)
            login(request, user)
            # нужен редирект на страницу профиля
            return redirect('/')
    else:
        if not request.user.is_authenticated:
            return redirect('/')
        # prepopulate fields with current user instance
        prepolulated_fields = ChangeUserForm.prepopulate(request.user)
        change_form = ChangeUserForm(initial=prepolulated_fields)
    return render(request, 'accounts/profile.html', {'change_form': change_form})

def change_password(request):
    user = request.user
    if request.method == "POST":
        password_form = SetPasswordForm(user, request.POST)
        if password_form.is_valid():
            password_form.save()
            return redirect('/')
        else:
            return render(request, 'accounts/changepassword.html', {'password_form': password_form})
    else:
        if not request.user.is_authenticated:
            return redirect('/')
        password_form = SetPasswordForm(user)
        return render(request, 'accounts/changepassword.html', {'password_form': password_form})
