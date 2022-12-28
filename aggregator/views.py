from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import PostForm, EditPostForm
from . import models
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.
def index(request):
    posts = models.Post.objects.prefetch_related('media_set')
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'aggregator/index.html', {'page': page_obj})

def my_posts(request):
    if not request.user.is_authenticated:
        return redirect('/')
    posts = models.Post.objects.prefetch_related('media_set').filter(user=request.user)
    print(posts)
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'aggregator/my_posts.html', {'page': page_obj})    

def show_post(request, post_id):
    if request.method == "POST":
        post_form = EditPostForm(request.POST, request.FILES)
        if post_form.is_valid():
            data = post_form.cleaned_data
            category = models.Category.objects.create(name=data['category'])
            subcategory = models.Subcategory.objects.create(name=data['subcategory'])
            # redacting post object
            models.Post.objects.select_related('category', 'subcategory', 'user').prefetch_related('media_set').filter(id=post_id).update(title=data['title'], description=data['description'],
                                                    category=category,
                                                    subcategory=subcategory, price=data['price'],
                                                    city = data['city'])
            post = models.Post.objects.select_related('category', 'subcategory', 'user').prefetch_related('media_set').get(id=post_id)
            prepolulated_fields = EditPostForm.prepopulate(post=post)
            post_form = EditPostForm(initial=prepolulated_fields)
            #return render(request, 'aggregator/post.html', {'post': post, 'post_form': post_form})
            return redirect('/myposts')
    else:
        post = models.Post.objects.select_related('category', 'subcategory', 'user').prefetch_related('media_set').get(id=post_id)
        prepolulated_fields = EditPostForm.prepopulate(post=post)
        post_form = EditPostForm(initial=prepolulated_fields)
        return render(request, 'aggregator/post.html', {'post': post, 'post_form': post_form})

def add_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
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
            # if there is a picture
            try:
                photo = request.FILES['photo']
                new_photo = models.Media.objects.create(name=photo.name, photo=photo, post_id=new_post.id)
                print(new_photo)
                return redirect('/')
            except MultiValueDictKeyError:
                # even if there is no picture we absolutely need to create blank one because of how 
                # index.html works
                new_photo = models.Media.objects.create(name=None, photo=None, post_id=new_post.id)
                # нужен редирект на мои объявления
                return redirect('/')
            
        else:
            return render(request, 'aggregator/addpost.html', {'post_form': post_form})
    else:
        if not request.user.is_authenticated:
            # нужно сделать редирект на главную страницу в идеале, где будет написано please login
            return redirect('/')
        post_form = PostForm()
        return render(request, 'aggregator/addpost.html', {'post_form': post_form})
