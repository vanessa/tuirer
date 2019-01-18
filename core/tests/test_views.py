from django.test import Client, TestCase
from django.urls import reverse


class HomeViewTest(TestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse("core:home")
        self.client = Client()

    def test_response_status_code_200(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
