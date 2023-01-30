import json

from django.contrib.auth.models import User
from django.test import TestCase, Client

from app.forms.test_login_form import LoginForm
from app.models import UserDetail, Category, Note


class ModelTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(password="12341234", username="test_user", email="test@test.com", id=1)
        UserDetail.objects.create(user=user)

    def test_increase(self):
        user_detail = UserDetail.objects.get(user_id=1)
        self.assertEqual(user_detail.note_count, 0)
        user_detail.increase_count()
        self.assertEqual(user_detail.note_count, 1)


class LoginFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(password="Votmxmzoavjtm123!", username="test_user1", email="abcd@email.com")
        UserDetail.objects.create(user=self.user)

    def test_login_form(self):
        form_data = {"email_or_username": "abcd@email.com", "password": "Votmxmzoavjtm123!"}
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())


class CategoryAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create(password="12341234", username="test_user", email="test@test.com")
        UserDetail.objects.create(user=self.user)
        category = Category.objects.create(name="test_category", user=self.user)
        Note.objects.create(title="test_note", content="test_content", category=category, user=self.user)

    def test_category_api(self):
        c = Client()
        c.force_login(self.user)

        res = c.get("/api/categories")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()[0]["name"], "test_category")
        self.assertEqual(res.json()[0]["id"], 1)
        print(res.json())

        category = {"name": "test_category2"}
        c.post("/api/categories", json.dumps(category), content_type="application/json")

        res = c.get("/api/categories")
        self.assertEqual(len(res.json()), 2)
        print(res.json())
