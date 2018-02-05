"""
Unit tests for the accounts application
"""
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.urls import resolve
from accounts.views import signup
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpTests(TestCase):
    """Unit tests for the signup page"""

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_url_resolves_signup_view(self):
        """Checks that the signup url resolves to the correct view"""
        view = resolve('/signup/')
        self.assertEqual(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserCreationForm)

    def test_form_inputs(self):
        """View must contain 5 inputs: crsf, username, email,
        password1, password2
        """
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="password"', 2)


class SuccessfulSignUpTests(TestCase):
    """Unit tests for for when a user successfully signs up"""

    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'email': 'john@doe.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

    def test_redirection(self):
        """
        A valid form submission should redirect the user to the home page
        """
        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        """
        Create a new request to an arbitrary page.
        The resulting response should now have a `user` to its context,
        after a successful sign up.
        """
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)


class InvalidSignupTests(TestCase):
    """Unit tests for invalid user creation"""
    def setUp(self):
        url = reverse('signup')
        # The user submits an empty form
        self.response = self.client.post(url, {})

    def test_signup_status_code(self):
        """Invalid form submission should return to the same page"""
        self.assertEqual(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

    def test_dont_create_user(self):
        """A user should not be created when an invalid form is submitted"""
        self.assertFalse(User.objects.exists())

