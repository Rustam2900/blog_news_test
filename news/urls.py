from django.urls import path
from .views import CategoryRetrieveModelMixin

urlpatterns = [
    # path('categories/', CategoryListModelMixin.as_view(), name='category-list'),
    path('categories/<slug>/', CategoryRetrieveModelMixin.as_view(), name='category-detail'),
]
