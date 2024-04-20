from django.db.models import Q, Min, Sum, Max, F
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

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


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


@api_view(['GET'])
def get_min_max_sum(request):
    '''
    Операции выполняются по обычной, а не скидочной цене
    '''
    min_price = Products.objects.aggregate(min=Min('price'))['min']
    max_price = Products.objects.aggregate(max=Max('price'))['max']
    balance_sum = Products.objects.aggregate(sum=Sum(F('price') * F('product_balance')))['sum']

    return Response({'min': min_price, 'max': max_price, 'sum': balance_sum})
