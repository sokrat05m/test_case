from django.core.mail import send_mail

from cart.models import Cart
from celery_app import app
from payments.utils import get_payment_link


@app.task()
def send_order_mail_task(cart_id: int, email: str) -> str:
    cart = Cart.objects.get(id=cart_id)

    response = get_payment_link(cart, email)
    subject = "Оплата"
    message = (f"Ссылка: {response['url']}, "
               f"номер заказа: {response['orderId']}")
    recipient_list = [email]
    try:
        send_mail(subject=subject,
                  message=message,
                  from_email=None,
                  recipient_list=recipient_list,
                  fail_silently=False)

        return 'Письмо успешно отправлено'
    except Exception as e:
        return f'Ошибка с отправкой письма: {str(e)}'
