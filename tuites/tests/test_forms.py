from tuites.forms import PostTuiteForm
from django.test import TestCase
from model_mommy import mommy


class PostTuiteFormTest(TestCase):
    def test_form_valid_correct_data(self):
        user = mommy.make("users.User")
        data = {
            "initial": {
                "creator": user.id
            },
            "data": {
                "creator": user.id,
                "content": "Conteúdo qualquer"
            }
        }
        form = PostTuiteForm(**data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        user_1 = mommy.make("users.User")
        user_2 = mommy.make("users.User")
        data = {
            "initial": {
                "creator": user_1.id
            },
            "data": {
                "creator": user_2.id,
                "content": "Conteúdo qualquer"
            }
        }
        form = PostTuiteForm(**data)
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors["creator"],
            ["Você está tentando burlar o sistema!"]
        )