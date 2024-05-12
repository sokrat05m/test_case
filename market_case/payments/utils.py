import requests
from django.db.models import Sum, F

from cart.models import Cart


def get_payment_link(cart: Cart, email: str) -> dict:
    url = 'http://test-payments.mediann-dev.ru/payment'
    query = cart.items.aggregate(
        sum=Sum(F('quantity') * F('product__discount_price')),
        quantity=Sum('quantity'))

    data = {
        'amount': query['sum'],
        'items_qty': query['quantity'],
        'api_token': 'jhgjebgy7w44bfgsfsjgjdgmjuiege',
        'user_email': email
    }
    response = requests.post(url, json=data)
    return response.json()


def verify_cart_items_before_order(cart: Cart) -> list:
    items = cart.items.all().select_related('product')
    missing_items = []
    for item in items:
        if item.quantity > item.product.product_balance:
            missing_items.append(f"'{item.product.product_name}'")

    return missing_items


def generate_missing_items_message(cart: Cart) -> str | None:
    missing_items = verify_cart_items_before_order(cart)

    if len(missing_items) > 1:
        return f"Продуктов {", ".join(missing_items)} нет в таком количестве"

    if len(missing_items) == 1:
        return f"Продукта '{missing_items[0]}' нет в таком количестве"

    return None


def clear_cart(cart: Cart):
    cart.items.all().delete()
