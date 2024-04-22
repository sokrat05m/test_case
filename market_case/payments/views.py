from celery.result import AsyncResult

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .tasks import mail


@api_view(['GET'])
def send_mail_test(request):
    email = request.user.email
    cart_id = request.user.cart.id
    result = mail.delay(cart_id, email)
    return Response({'message': result.get()})
