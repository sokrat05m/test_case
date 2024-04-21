from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from products.models import Products, Category, Subcategory
from products.serializers import ProductSerializer


# Create your tests here.

class ProductsTest(APITestCase):

    def test_get_list(self):
        category_1 = Category.objects.create(category_name='Автомобили')
        sub_category_1 = Subcategory.objects.create(subcategory_name='Седаны',
                                                    parent=category_1)
        product_1 = Products.objects.create(product_name='Тойота Камри',
                                            price=6000, discount_price=5000,
                                            product_balance=7, product_characteristics='Камри',
                                            product_category=category_1, product_subcategory=sub_category_1)

        category_2 = Category.objects.create(category_name='Товары для животных')
        sub_category_2 = Subcategory.objects.create(subcategory_name='Переноски',
                                                    parent=category_2)
        product_2 = Products.objects.create(product_name='Перенсока красная',
                                            price=300, discount_price=280,
                                            product_balance=7, product_characteristics='Обычная переноска',
                                            product_category=category_2, product_subcategory=sub_category_2)

        url = reverse('products:products')
        res = self.client.get(url)
        response_data = res.data.get('results')
        self.assertEqual(status.HTTP_200_OK, res.status_code)
        self.assertEqual(ProductSerializer([product_1, product_2], many=True).data, response_data)

    def test_get_min_max_sum(self):
        category_1 = Category.objects.create(category_name='Автомобили')
        sub_category_1 = Subcategory.objects.create(subcategory_name='Седаны',
                                                    parent=category_1)
        product_1 = Products.objects.create(product_name='Тойота Камри',
                                            price=6000, discount_price=5000,
                                            product_balance=7, product_characteristics='Камри',
                                            product_category=category_1, product_subcategory=sub_category_1)

        category_2 = Category.objects.create(category_name='Товары для животных')
        sub_category_2 = Subcategory.objects.create(subcategory_name='Переноски',
                                                    parent=category_2)
        product_2 = Products.objects.create(product_name='Перенсока красная',
                                            price=300, discount_price=280,
                                            product_balance=7, product_characteristics='Обычная переноска',
                                            product_category=category_2, product_subcategory=sub_category_2)

        url = reverse('products:min_max_sum')
        res = self.client.get(url)
        self.assertEqual({'min': 300, 'max': 6000, 'sum': 44100}, res.data)
