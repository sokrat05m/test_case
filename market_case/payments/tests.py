from django.contrib.auth.models import User
from django.test import TestCase

import requests
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from cart.models import Cart, CartItem
from products.models import Category, Subcategory, Products


class PaymentsTest(TestCase):

    def test_get_response(self):
        url = 'http://test-payments.mediann-dev.ru/payment'
        data = {
            'amount': 100,
            'items_qty': 10,
            'api_token': 'jhgjebgy7w44bfgsfsjgjdgmjuiege',
            'user_email': 'test@mail.ru'
        }
        response = requests.post(url, json=data)
        self.assertEqual(100, response.json()['amount'])
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_check_item_quantity(self):
        category_1 = Category.objects.create(category_name='Автомобили')
        sub_category_1 = Subcategory.objects.create(subcategory_name='Седаны',
                                                    parent=category_1)
        product_1 = Products.objects.create(product_name='Тойота Камри',
                                            price=6000, discount_price=5000,
                                            product_balance=7, product_characteristics='Камри',
                                            product_category=category_1, product_subcategory=sub_category_1)

        user_1 = User.objects.create_user(username='testuser', password='12345')
        cart_1 = Cart.objects.create(user=user_1)
        cart_items = CartItem.objects.create(cart=cart_1, product=product_1, quantity=10)
        url = reverse('payments:payment')
        self.client.force_login(user_1)
        res = self.client.get(url)
        self.assertEqual({'message': 'Продукта Тойота Камри нет в таком количестве'}, res.data)
