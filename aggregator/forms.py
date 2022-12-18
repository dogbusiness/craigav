from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from aggregator.models import Category, Subcategory, Post, Media
from .categories import CATEGORIES, SUBCATEGORIES
# ПОПРАВЬ ИМПОРТЫ

# class PostForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     description = forms.CharField(max_length=1500)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
#     subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True)
#     price = forms.DecimalField(max_digits=12, decimal_places=2)
#     city = forms.CharField(max_length=200)

# They should look like a single
class CategoryForm(ModelForm):
    name = forms.ChoiceField(label='Category', choices=CATEGORIES)

    class Meta:
        model = Category
        fields = ['name']

class SubCategoryForm(ModelForm):
    name = forms.ChoiceField(label='SubCategory', choices=SUBCATEGORIES)
    class Meta:
        model = Subcategory
        fields = ['name']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'price', 'city']

# Class MediaForm(ModelForm)
