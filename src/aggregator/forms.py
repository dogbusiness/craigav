from django import forms

from .categories import CATEGORIES, SUBCATEGORIES


class PostForm(forms.Form):
    title = forms.CharField(max_length=50)
    category = forms.ChoiceField(label="Category", choices=CATEGORIES)
    subcategory = forms.ChoiceField(label="SubCategory", choices=SUBCATEGORIES)
    price = forms.DecimalField(max_digits=12, decimal_places=2, min_value=0.01)
    city = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea, max_length=1500)
    photo = forms.ImageField(required=False)

    def prepopulate(post):
        initial_in_fields = {
            "title": post.title,
            "category": post.category,
            "subcategory": post.subcategory,
            "price": post.price,
            "city": post.city,
            "description": post.description,
        }
        return initial_in_fields


class EditPostForm(forms.Form):
    title = forms.CharField(max_length=50)
    category = forms.ChoiceField(label="Category", choices=CATEGORIES)
    subcategory = forms.ChoiceField(label="SubCategory", choices=SUBCATEGORIES)
    price = forms.DecimalField(max_digits=12, decimal_places=2, min_value=0.01)
    city = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea, max_length=1500)

    def prepopulate(post):
        initial_in_fields = {
            "title": post.title,
            "category": post.category,
            "subcategory": post.subcategory,
            "price": post.price,
            "city": post.city,
            "description": post.description,
        }
        return initial_in_fields
