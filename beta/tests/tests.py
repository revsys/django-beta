from django.conf import settings
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
    pass 

