from django.core.mail import send_mail
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from payments.utils import get_payment_link, check_item_quantity, clear_cart


@api_view(['GET'])
def send_mail_test(request):
    if request.user.cart.items.all():
        response = get_payment_link(request)
        subject = "Оплата"
        message = f"Ссылка: {response['url']}, номер заказа: {response['orderId']}"
        recipient_list = [request.user.email]
        check = check_item_quantity(request)
        if check:
            return Response({'message': f'Продукта {check} нет в таком количестве'})
        try:
            send_mail(subject=subject,
                      message=message,
                      from_email=None,
                      recipient_list=recipient_list,
                      fail_silently=False)
            clear_cart(request)
            return Response({'message': 'Письмо успешно отправлено'})
        except Exception as e:
            return Response({'message': f'Ошибка с отправкой письма: {str(e)}'},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response({'message': 'Пустая корзина'})
