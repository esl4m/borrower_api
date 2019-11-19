from django.test import TestCase, Client
from .models import Borrower


class BorrowerTest(TestCase):
    """ Test module for Borrower model """

    def setUp(self):
        self.borrower_url = '/api/borrower/'
        self.client = Client()

        self.name = 'borrower_1'

        Borrower.objects.create(
            name='borrower_1', amount=5000.0, period=6)


    def test_get_all_borrowers(self):
        response = self.client.get(self.borrower_url)
        self.assertEqual(response.status_code, 200)
