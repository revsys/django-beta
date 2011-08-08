from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from django.db import IntegrityError

from beta.models import BetaSignup
from beta.forms import BetaSignupForm 

class BetaModelTests(TestCase):

    def test_simple_creation(self):
        self.assertTrue(BetaSignup.objects.create(email='foo@bar.com'))
        self.assertTrue(BetaSignup.objects.create(email='foo1@bar.com', first_name='Frank'))
        self.assertTrue(BetaSignup.objects.create(email='foo2@bar.com', first_name='Frank', last_name='Wiles'))

    def test_duplicate_creation(self):
        """ Ensure we can't register twice """
        first = BetaSignup.objects.create(email='foo@bar.com')
        self.assertRaises(IntegrityError, BetaSignup.objects.create, email='foo@bar.com')

class BetaFormEmailTests(TestCase):
    """ Test our somewhat complicated form """

    def test_email_only(self):
        data = {'email': 'foo@bar.com'}
        form = BetaSignupForm(data)
        self.assertTrue(form.is_valid())

class BetaFormFirstTests(TestCase):

    def setUp(self):
        settings.BETA_CAPTURE_FIRST = True 

    def test_capture_first(self):
        data = {'email': 'foo@bar.com'}
        form = BetaSignupForm(data)
        self.assertFalse(form.is_valid())

        data['first_name'] = 'Bob'
        form = BetaSignupForm(data)
        self.assertTrue(form.is_valid())

    def tearDown(self):
        settings.BETA_CAPTURE_FIRST = False 

class BetaFormBoth(TestCase):

    def setUp(self):
        settings.BETA_CAPTURE_BOTH = True 

    def test_capture_first(self):
        data = {'email': 'foo@bar.com'}
        form = BetaSignupForm(data)
        self.assertFalse(form.is_valid())

        data['first_name'] = 'Bob'
        form = BetaSignupForm(data)
        self.assertFalse(form.is_valid())

        data['last_name'] = 'Smith'
        form = BetaSignupForm(data)
        self.assertTrue(form.is_valid())

    def tearDown(self):
        settings.BETA_CAPTURE_BOTH = False 

class BetaViewTests(TestCase):

    def test_view_creation(self):
        response = self.client.get(reverse('beta_signup'))
        self.assertEqual(response.status_code, 200) 

        data = {'email': 'foo@bar.com'}
        response = self.client.post(reverse('beta_signup'), data)
        self.assertRedirects(response, reverse('beta_confirmation'))

        self.assertEqual(BetaSignup.objects.all().count(), 1)
        foo = BetaSignup.objects.get(email='foo@bar.com')
        self.assertTrue(foo)


class BetaListenerTest(TestCase):

    def test_listener(self):
        b = BetaSignup.objects.create(email='foo12@bar.com')
        u = User.objects.create_user('foo12', 'foo12@bar.com', 'testpass')
        b2 = BetaSignup.objects.get(email='foo12@bar.com')
        self.assertTrue(b2.registered)
