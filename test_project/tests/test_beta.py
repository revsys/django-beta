from django.apps import apps
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.test import TestCase, override_settings
from django.urls import reverse

import pytest

from beta.forms import BetaSignupForm
from beta.models import BetaSignup


def test_app_is_installed():
    """Smoke test: the beta app is importable and installed."""
    assert apps.is_installed("beta")
    assert apps.get_model("beta", "BetaSignup") is BetaSignup


class BetaModelTests(TestCase):
    def test_simple_creation(self):
        self.assertTrue(BetaSignup.objects.create(email="foo@bar.com"))
        self.assertTrue(BetaSignup.objects.create(email="foo1@bar.com", first_name="Frank"))
        self.assertTrue(BetaSignup.objects.create(email="foo2@bar.com", first_name="Frank", last_name="Wiles"))

    def test_str(self):
        signup = BetaSignup.objects.create(email="foo@bar.com")
        self.assertEqual(str(signup), "Beta Signup - foo@bar.com")

    def test_duplicate_creation(self):
        """Ensure we can't register twice"""
        BetaSignup.objects.create(email="foo@bar.com")
        with self.assertRaises(IntegrityError):
            BetaSignup.objects.create(email="foo@bar.com")


class BetaManagerTests(TestCase):
    def test_manager_methods(self):
        BetaSignup.objects.create(email="a@bar.com", contacted=True, registered=True)
        BetaSignup.objects.create(email="b@bar.com", contacted=False, registered=False)

        self.assertEqual(BetaSignup.objects.contacted().count(), 1)
        self.assertEqual(BetaSignup.objects.not_contacted().count(), 1)
        self.assertEqual(BetaSignup.objects.registered().count(), 1)
        self.assertEqual(BetaSignup.objects.not_registered().count(), 1)


class BetaFormEmailTests(TestCase):
    """Test our somewhat complicated form"""

    def test_email_only(self):
        form = BetaSignupForm({"email": "foo@bar.com"})
        self.assertTrue(form.is_valid())


@override_settings(BETA_CAPTURE_FIRST=True)
class BetaFormFirstTests(TestCase):
    def test_capture_first(self):
        form = BetaSignupForm({"email": "foo@bar.com"})
        self.assertFalse(form.is_valid())

        form = BetaSignupForm({"email": "foo@bar.com", "first_name": "Bob"})
        self.assertTrue(form.is_valid())


@override_settings(BETA_CAPTURE_BOTH=True)
class BetaFormBothTests(TestCase):
    def test_capture_both(self):
        form = BetaSignupForm({"email": "foo@bar.com"})
        self.assertFalse(form.is_valid())

        form = BetaSignupForm({"email": "foo@bar.com", "first_name": "Bob"})
        self.assertFalse(form.is_valid())

        form = BetaSignupForm({"email": "foo@bar.com", "first_name": "Bob", "last_name": "Smith"})
        self.assertTrue(form.is_valid())


class BetaViewTests(TestCase):
    def test_view_creation(self):
        response = self.client.get(reverse("beta_signup"))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse("beta_signup"), {"email": "foo@bar.com"})
        self.assertRedirects(response, reverse("beta_confirmation"))

        self.assertEqual(BetaSignup.objects.count(), 1)


class BetaListenerTests(TestCase):
    def test_listener_marks_registered(self):
        BetaSignup.objects.create(email="foo12@bar.com")
        User.objects.create_user("foo12", "foo12@bar.com", "testpass")
        signup = BetaSignup.objects.get(email="foo12@bar.com")
        self.assertTrue(signup.registered)


pytestmark = pytest.mark.django_db
