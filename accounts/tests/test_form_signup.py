"""Unit tests for the accounts signup forms"""
from django.test import TestCase
from accounts.forms import SignUpForm

class SignUpFormTest(TestCase):
    """Unit tests for the SignUpForm class"""
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2']
        actual = list(form.fields)
        self.assertEqual(expected, actual)
