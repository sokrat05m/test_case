from typing import NoReturn

import requests

from rest_framework import status
from rest_framework.test import APITestCase


class PaymentsTest(APITestCase):

    def setUp(self):
        self.url = 'http://test-payments.mediann-dev.ru/payment'
        self.data = {
            'amount': 100,
            'items_qty': 10,
            'api_token': 'jhgjebgy7w44bfgsfsjgjdgmjuiege',
            'user_email': 'test@mail.ru'
        }

    def test_get_response(self) -> NoReturn:
        response = requests.post(self.url, json=self.data)
        self.assertEqual(100, response.json()['amount'])
        self.assertEqual(status.HTTP_200_OK, response.status_code)
