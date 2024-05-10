
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from .tasks import send_order_mail_task
from .utils import check_item_quantity, clear_cart


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def send_order_detail_mail(request: Request) -> Response:
    email = request.user.email
    cart = request.user.cart
    check_items = check_item_quantity(cart)
    if check_items:
        return Response({'message': check_items})
    if cart.items.exists():
        result = send_order_mail_task.delay(cart.id, email).get()
        if result == 'Письмо успешно отправлено':
            clear_cart(cart)
        message = result

    else:
        message = 'Пустая корзина'

    return Response({'message': message})
