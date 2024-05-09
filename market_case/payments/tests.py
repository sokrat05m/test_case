from django.contrib.auth.models import User
from django.test import TestCase

import requests
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from cart.models import Cart, CartItem
from products.models import Category, Subcategory, Products


class PaymentsTest(APITestCase):

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

    # def test_check_item_quantity(self):
    #     url = reverse('payments:payment')
    #     category_2 = Category.objects.create(category_name='Автомобили')
    #     sub_category_2 = Subcategory.objects.create(subcategory_name='Седаны',
    #                                                 parent=category_2)
    #     product_2 = Products.objects.create(product_name='Тойота Камри',
    #                                         price=6000, discount_price=5000,
    #                                         product_balance=7, product_characteristics='Камри',
    #                                         product_category=category_2, product_subcategory=sub_category_2)
    #
    #     user_2 = User.objects.create_user(username='testuser', password='12345', email='test@mail.ru')
    #     cart_2 = Cart.objects.create(user=user_2)
    #     cart_items = CartItem.objects.create(cart=cart_2, product=product_2, quantity=10)
    #     self.client.force_login(user_2)
    #     res = self.client.get(url)
    #     self.assertEqual(status.HTTP_200_OK, res.status_code)
    #     # self.assertEqual({'message': 'Продукта Тойота Камри нет в таком количестве'}, res.data)
