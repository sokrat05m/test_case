from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token

# Create your tests here.
from rest_framework.test import APITestCase, APIClient

from cart.models import Cart, CartItem
from cart.serializers import CartSerializer
from products.models import Category, Subcategory, Products


class CartTest(APITestCase):
    def test_get_cart(self):
        category_1 = Category.objects.create(category_name='Автомобили')
        sub_category_1 = Subcategory.objects.create(subcategory_name='Седаны',
                                                    parent=category_1)
        product_1 = Products.objects.create(product_name='Тойота Камри',
                                            price=6000, discount_price=5000,
                                            product_balance=7, product_characteristics='Камри',
                                            product_category=category_1, product_subcategory=sub_category_1)

        user_1 = User.objects.create_user(username='testuser', password='12345')
        cart_1 = Cart.objects.create(user=user_1)
        url = reverse('cart:add_cart')
        self.client.force_login(user_1)
        res = self.client.post(url, data={"product_id": 1, "quantity": 3}, format='json')
        self.assertEqual(CartSerializer(cart_1).data, res.data)


