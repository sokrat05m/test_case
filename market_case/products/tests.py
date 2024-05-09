from django.db.models import Q
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from products.models import Products, Category, Subcategory
from products.serializers import ProductSerializer
from products.views import ProductListByCategoryAPIView


# Create your tests here.

class ProductsTest(APITestCase):
    def setUp(self):
        self.category_1 = Category.objects.create(category_name='Автомобили')
        self.sub_category_1 = Subcategory.objects.create(subcategory_name='Седаны',
                                                         parent=self.category_1)
        self.product_1 = Products.objects.create(product_name='Тойота Камри',
                                                 price=6000, discount_price=5000,
                                                 product_balance=7, product_characteristics='Камри',
                                                 product_category=self.category_1,
                                                 product_subcategory=self.sub_category_1)

        self.category_2 = Category.objects.create(category_name='Товары для животных')
        self.sub_category_2 = Subcategory.objects.create(subcategory_name='Переноски',
                                                         parent=self.category_2)
        self.product_2 = Products.objects.create(product_name='Перенсока красная',
                                                 price=300, discount_price=280,
                                                 product_balance=7, product_characteristics='Обычная переноска',
                                                 product_category=self.category_2,
                                                 product_subcategory=self.sub_category_2)

    def test_get_list(self):
        url = reverse('products:products')
        res = self.client.get(url)
        response_data = res.data.get('results')

        self.assertEqual(status.HTTP_200_OK, res.status_code)
        self.assertEqual(ProductSerializer([self.product_1, self.product_2], many=True).data, response_data)

    def test_get_min_max_sum_price(self):
        url = reverse('products:min_max_sum')
        res = self.client.get(url)
        self.assertEqual({'min': 300, 'max': 6000, 'sum': 44100}, res.data)



