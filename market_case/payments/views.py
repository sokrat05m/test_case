

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from .tasks import send_order_mail_task
from .utils import check_item_quantity


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def send_order_detail_mail(request: Request) -> Response:
    email = request.user.email
    cart = request.user.cart
    check = check_item_quantity(cart)
    if check:
        return Response(
            {'message': f"Продукта '{check}' нет в таком количестве"}
        )
    result = send_order_mail_task.delay(cart.id, email)
    return Response({'message': result.get()})
