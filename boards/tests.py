"""
Unit tests for boards application
"""
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from boards.views import home


class HomeTests(TestCase):

    """
    Unit tests for the Home page
    """

    def test_home_view_status(self):
        """
        Tests the home view returns a 200 status
        """
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)
