

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from .tasks import send_order_mail_task


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def send_order_detail_mail(request: Request) -> Response:
    email = request.user.email
    cart_id = request.user.cart.id
    print(email)
    result = send_order_mail_task.delay(cart_id, email)
    return Response({'message': result.get()})
