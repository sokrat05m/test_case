from typing import NoReturn

from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase

from cart.models import Cart
from cart.serializers import CartSerializer
from products.models import Category, Subcategory, Product


class CartTest(APITestCase):
    def setUp(self) -> NoReturn:
        self.category_1 = Category.objects.create(
            category_name='Автомобили'
        )
        self.sub_category_1 = Subcategory.objects.create(
            subcategory_name='Седаны',
            parent=self.category_1
        )
        self.product_1 = Product.objects.create(
            product_name='Тойота Камри',
            price=6000,
            discount_price=5000,
            product_balance=7,
            product_characteristics='Камри',
            product_category=self.category_1,
            product_subcategory=self.sub_category_1
        )

        self.user_1 = User.objects.create_user(
            username='testuser',
            password='12345'
        )
        self.cart_1 = Cart.objects.create(
            user=self.user_1
        )

    def test_get_cart(self) -> NoReturn:
        url = reverse('cart:add_cart')
        self.client.force_login(self.user_1)
        res = self.client.post(
            url, data={"product_id": 1, "quantity": 3},
            format='json'
        )
        self.assertEqual(CartSerializer(self.cart_1).data, res.data)
