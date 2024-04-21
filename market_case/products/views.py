from django.db.models import Q, Min, Sum, Max, F
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Products, Category
from .serializers import ProductSerializer, CategorySerializer


# Create your views here.
class ProductsAPIListPagination(PageNumberPagination):
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
    queryset = Products.objects.all().select_related()
    serializer_class = ProductSerializer


@api_view(['GET'])
def get_min_max_sum(request):
    '''
    Операции выполняются по обычной, а не скидочной цене
    '''
    total = Products.objects.aggregate(min=Min('price'), max=Max('price'),
                                       sum=Sum(F('price') * F('product_balance')))

    return Response({'min': total['min'], 'max': total['max'], 'sum': total['sum']})
