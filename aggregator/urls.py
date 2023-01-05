from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from aggregator import views

urlpatterns = [
    path('', views.index, name='index'),
    path('q/', views.search_post, name='search_post'),
    path('myposts', views.my_posts, name='my_posts'),
    path('post/<int:post_id>', views.show_post, name='show_post'),
    path('addpost', views.add_post, name='add_post'),
    path('deletepost/<int:post_id>', views.delete_post, name='delete_post'),
    path('about', views.about, name='about')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)