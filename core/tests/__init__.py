from django.test import TestCase, Client
from django.urls import reverse


class TestHomeView(TestCase):
    def setUp(self):
        self.view_url = reverse('core:home')
    
    def test_status_code_200(self):
        response = self.client.get(self.view_url)
        self.assertEqual(response.status_code, 200)
