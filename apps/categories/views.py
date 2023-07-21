from rest_framework.filters import SearchFilter

from .models import Category
from .serializers import CategorySerializer
from rest_framework import generics


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