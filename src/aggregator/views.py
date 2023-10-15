from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import redirect, render
from django.utils.datastructures import MultiValueDictKeyError

from . import models
from .forms import EditPostForm, PostForm


def search_post(request):
    if request.method == "GET":
        title = request.GET.get("title")
        category = request.GET.get("category")
        subcategory = request.GET.get("subcategory")
        city = request.GET.get("city")

        posts = (
            models.Post.objects.select_related("category", "subcategory", "user")
            .prefetch_related("media_set")
            .all()
        )
        if title != "":
            posts = posts.filter(Q(title__icontains=title))
        if category != "":
            posts = posts.filter(Q(category__name=category))
        if subcategory != "":
            posts = posts.filter(Q(subcategory__name=subcategory))
        if city != "":
            posts = posts.filter(Q(city__icontains=city))

        posts = posts.order_by("id")

        paginator = Paginator(posts, 3)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = {
            "page": page_obj,
            "title": title,
            "category": category,
            "subcategory": subcategory,
            "city": city,
        }
        return render(request, "aggregator/search_post.html", context=context)


def index(request):
    posts = models.Post.objects.prefetch_related("media_set")
    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "aggregator/index.html", {"page": page_obj})


def my_posts(request):
    if not request.user.is_authenticated:
        return redirect("/")
    posts = models.Post.objects.prefetch_related("media_set").filter(user=request.user)
    paginator = Paginator(posts, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "aggregator/my_posts.html", {"page": page_obj})


def show_post(request, post_id):
    if request.method == "POST":
        post_form = EditPostForm(request.POST, request.FILES)
        if post_form.is_valid():
            data = post_form.cleaned_data
            category = models.Category.objects.create(name=data["category"])
            subcategory = models.Subcategory.objects.create(name=data["subcategory"])
            models.Post.objects.select_related(
                "category", "subcategory", "user"
            ).prefetch_related("media_set").filter(id=post_id).update(
                title=data["title"],
                description=data["description"],
                category=category,
                subcategory=subcategory,
                price=data["price"],
                city=data["city"],
            )
            post = (
                models.Post.objects.select_related("category", "subcategory", "user")
                .prefetch_related("media_set")
                .get(id=post_id)
            )
            prepolulated_fields = EditPostForm.prepopulate(post=post)
            post_form = EditPostForm(initial=prepolulated_fields)
            return redirect("/myposts")
    else:
        post = (
            models.Post.objects.select_related("category", "subcategory", "user")
            .prefetch_related("media_set")
            .get(id=post_id)
        )
        prepolulated_fields = EditPostForm.prepopulate(post=post)
        post_form = EditPostForm(initial=prepolulated_fields)
        return render(
            request, "aggregator/post.html", {"post": post, "post_form": post_form}
        )


def add_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            data = post_form.cleaned_data
            category = models.Category.objects.create(name=data["category"])
            subcategory = models.Subcategory.objects.create(name=data["subcategory"])
            new_post = models.Post.objects.create(
                title=data["title"],
                description=data["description"],
                user=request.user,
                category=category,
                subcategory=subcategory,
                price=data["price"],
                city=data["city"],
            )
            try:
                photo = request.FILES["photo"]
                new_photo = models.Media.objects.create(
                    name=photo.name, photo=photo, post_id=new_post.id
                )
                return redirect("/")
            except MultiValueDictKeyError:
                new_photo = models.Media.objects.create(  # noqa: F841
                    name=None, photo=None, post_id=new_post.id
                )
                return redirect("/")

        else:
            return render(request, "aggregator/addpost.html", {"post_form": post_form})
    else:
        if not request.user.is_authenticated:
            return redirect("/")
        post_form = PostForm()
        return render(request, "aggregator/addpost.html", {"post_form": post_form})


def delete_post(request, post_id):
    if not request.user.is_authenticated:
        return redirect("/")
    post_to_delete = (
        models.Post.objects.select_related("category", "subcategory", "user")
        .prefetch_related("media_set")
        .get(id=post_id)
    )
    if post_to_delete.user.id != request.user.id:
        raise PermissionDenied()
    else:
        post_to_delete.delete()
        return redirect("/myposts")


def about(request):
    return render(request, "aggregator/about.html")
