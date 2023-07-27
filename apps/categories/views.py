from rest_framework.filters import SearchFilter
from rest_framework import generics

from apps.categories.models import Category
from apps.categories.serializers import CategorySerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.filter(parent__isnull=True). \
        select_related('parent'). \
        prefetch_related('children',
                        'children__children',
                        'children__children__children')
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


class CategoryRetrieve(generics.RetrieveAPIView):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer
