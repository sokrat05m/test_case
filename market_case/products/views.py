from django.db.models import Q, Min, Sum, Max, F, QuerySet

from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


# Create your views here.
class ProductsAPIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 100


class ProductsAPIList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductsAPIListPagination


class ProductListByCategoryAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self) -> QuerySet:
        category_id = self.kwargs['category_id']
        queryset = Product.objects.filter(
            Q(product_category_id=category_id) |
            Q(product_subcategory__parent_id=category_id)).select_related('subcategory')
        print(type(queryset))
        return queryset


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


@api_view(['GET'])
def get_min_max_sum_price(request: Request) -> Response:
    """
    Операции выполняются по обычной, а не скидочной цене
    """
    query = Product.objects.aggregate(
        min=Min('price'), max=Max('price'),
        sum=Sum(F('price') * F('product_balance'))
    )

    return Response(
        {'min': query['min'], 'max': query['max'],
         'sum': query['sum']}, status=status.HTTP_200_OK
    )
