from django.test import TestCase, Client
from model_mommy import mommy
from django.urls import reverse


class PostTuiteViewTest(TestCase):
    def setUp(self):
        super().setUp()
        self.user = mommy.prepare("users.User", username="pantoja")
        self.user.set_password("projota123")
        self.user.save()

        self.client = Client()
        self.auth_client = Client()
        self.auth_client.login(
            username=self.user.username,
            password="projota123"
        )

        self.url = reverse("tuites:post")
        
    def test_logged_in_status_200(self):
        response = self.auth_client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_logged_out_status_302(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
