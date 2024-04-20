from django.core.mail import send_mail
from django.db.models import Sum, F
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from cart.serializers import CartSerializer
from payments.serializers import MailSerializer


# Create your views here.

@api_view(['GET'])
def send_mail_test(request):
    cart = request.user.cart
    email1 = 'ooosokrat@mail.ru'
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
    response = response.json()
    subject = "Оплата"
    message = f"Ссылка: {response['url']}, номер заказа: {response['orderId']}"
    recipient_list = ['ooosokrat@mail.ru']
    send_mail(
        subject=subject,
        message=message,
        from_email=None,
        recipient_list=recipient_list,
        fail_silently=False)
    return Response({
        'subject': subject,
        'message': message,
        'rec': recipient_list},
        status=status.HTTP_200_OK)

