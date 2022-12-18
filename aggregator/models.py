from django.db import models
from.categories import CATEGORIES, SUBCATEGORIES # for choices
from django.contrib.auth.models import User

# Categories
class Category(models.Model):
    name = models.CharField(max_length=31, choices=CATEGORIES)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, choices=SUBCATEGORIES)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

# Posts and Media
class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    city = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.title}, {self.description}, {self.price}'


class Media(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/')

    def __str__(self):
        return f'{self.post}, {self.file_name}'       