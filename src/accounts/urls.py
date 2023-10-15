from django.urls import path

from accounts import views

urlpatterns = [
    path("login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("register/", views.user_register, name="user_register"),
    path("profile/", views.change_profile, name="change_profile"),
    path("changepassword", views.change_password, name="change_password"),
]
