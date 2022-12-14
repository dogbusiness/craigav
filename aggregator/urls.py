from django.urls import path
from aggregator import views

urlpatterns = [
    path('', views.index, name='index')
]