from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from aggregator import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.show_post, name='show_post'),
    path('addpost', views.add_post, name='add_post')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)