from rest_framework.generics import ListAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from news.models import Category
from news.serializer import CategorySerializer


# class CategoryListAPIView(ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class CategoryRetrieveAPIView(RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field = 'slug'


class CategoryRetrieveModelMixin(ListModelMixin,
                                 RetrieveModelMixin,
                                 GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
