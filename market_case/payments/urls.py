from django.urls import path

from payments import views

app_name = 'payments'

urlpatterns = [
    path('pay/', views.send_order_detail_mail, name='payment'),
]
