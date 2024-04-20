from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase

from products.models import Products, Category, Subcategory
from products.serializers import ProductSerializer


# Create your tests here.

class ProductsTest(APITestCase):
    def test_get(self):
        category_1 = Category.objects.create(category_name='Автомобили')
        sub_category_1 = Subcategory.objects.create(subcategory_name='Седаны',
                                                    parent_id=1)
        product_1 = Products.objects.create(product_name='Тойота Камри',
                                            price=6000, discount_price=5000,
                                            product_balance=7, product_characteristics='Обычная гиря',
                                            product_category_id=1, product_subcategory_id=1)

        url = reverse('products:products')
        res = self.client.get(url)
        response_data = res.data.get('results')
        self.assertEqual(ProductSerializer([product_1], many=True).data, response_data)
