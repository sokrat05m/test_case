
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from cart.models import Cart, CartItem
from cart.serializers import CartSerializer
from products.models import Product


@api_view(['POST'])
def add_product_to_cart(request: Request) -> Response:
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)

    user = request.user

    try:
        cart = user.cart
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=user)
    product = Product.objects.get(pk=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product=product
    )
    if not created:
        cart_item.quantity += quantity
    else:
        cart_item.quantity = quantity
    cart_item.save()

    cart_serializer = CartSerializer(cart)
    return Response(cart_serializer.data, status=status.HTTP_200_OK)
