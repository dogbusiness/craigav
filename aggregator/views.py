from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import PostForm
from . import models

# Create your views here.
def index(request):
    posts = models.Post.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'aggregator/index.html', {'page': page_obj})

def show_post(request, post_id):
    #post = models.Post.objects.get(id=post_id)
    post = models.Post.objects.select_related('category', 'subcategory', 'user').get(id=post_id)
    return render(request, 'aggregator/post.html', {'post': post})

def add_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            data = post_form.cleaned_data
            # order of object creation: category -> subcategory -> post
            # categories, categories and user must be INSTANCES
            category = models.Category.objects.create(name=data['category'])
            subcategory = models.Subcategory.objects.create(name=data['subcategory'])
            new_post = models.Post.objects.create(title=data['title'], description=data['description'],
                                                    user=request.user, category=category,
                                                    subcategory=subcategory, price=data['price'],
                                                    city = data['city'])
            # нужен редирект на "мои объявления"
            return redirect('/')
    else:
        if not request.user.is_authenticated:
            # нужно сделать редирект на главную страницу в идеале, где будет написано please login
            return redirect('/')
        post_form = PostForm()
        return render(request, 'aggregator/addpost.html', {'post_form': post_form})
