from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from aggregator.models import Category, Subcategory, Post, Media
from .categories import CATEGORIES, SUBCATEGORIES
# ПОПРАВЬ ИМПОРТЫ

# single form for creating posts
class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    category = forms.ChoiceField(label='Category', choices=CATEGORIES)
    subcategory = forms.ChoiceField(label='SubCategory', choices=SUBCATEGORIES)
    price = forms.DecimalField(max_digits=12, decimal_places=2)
    city = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea, max_length=1500)
    # photo