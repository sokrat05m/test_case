from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Products
from .serializers import ProductSerializer


# Create your views here.
class ProductsAPIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 100


class ProductsAPIList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductsAPIListPagination


class ProductListByCategoryAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        queryset = Products.objects.filter(
            Q(product_category=category_id) |
            Q(product_subcategory__parent_id=category_id)).select_related()
        return queryset
