from django.shortcuts import render, redirect
from .forms import CategoryForm, SubCategoryForm, PostForm

# Create your views here.
def index(request):
    return render(request, 'aggregator/index.html')

def add_post(request):
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        subcategory_form = SubCategoryForm(request.POST)
        post_form = PostForm(request.POST)
    else:
        if not request.user.is_authenticated:
            # нужно сделать редирект на главную страницу в идеале, где будет написано please login
            return redirect('/')
        category_form = CategoryForm()
        subcategory_form = SubCategoryForm()
        post_form = PostForm()
        return render(request, 'aggregator/addpost.html', {'category_form': category_form, 
                                                            'subcategory_form' : subcategory_form,
                                                            'post_form': post_form})
