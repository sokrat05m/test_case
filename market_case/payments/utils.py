import requests
from django.db.models import Sum, F


def get_payment_link(request):
    cart = request.user.cart
    email1 = request.user.email
    url = 'http://test-payments.mediann-dev.ru/payment'
    query = cart.items.aggregate(sum=Sum(F('quantity') * F('product__discount_price')),
                                 quantity=Sum('quantity'))

    data = {
        'amount': query['sum'],
        'items_qty': query['quantity'],
        'api_token': 'jhgjebgy7w44bfgsfsjgjdgmjuiege',
        'user_email': email1
    }
    response = requests.post(url, json=data)
    return response.json()


def check_item_quantity(request):
    '''
    Проверка перед заказом, не превышает ли количество товара в заказе его остаток на складе
    '''
    cart = request.user.cart
    items = cart.items.all()
    for item in items:
        if item.quantity > item.product.product_balance:
            return item.product.product_name
    return None


def clear_cart(request):
    cart = request.user.cart
    cart.items.all().delete()
