from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views_django

urlpatterns = [
    path('', views_django.post_list, name='post_list'),
    path('post/<int:pk>/', views_django.post_detail, name='post_detail'),
    path('post/new/', views_django.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views_django.post_update, name='post_update'),
    path('post/<int:pk>/delete/', views_django.post_delete, name='post_delete'),
    path('post/<int:pk>/rate/', views_django.add_rating, name='add_rating'),
    path('categories/', views_django.category_list, name='category_list'),
    path('tags/', views_django.tag_list, name='tag_list')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
