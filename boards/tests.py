"""
Unit tests for boards application
"""
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from boards.views import home, board_topics
from boards.models import Board


class HomeTests(TestCase):

    """
    Unit tests for the Home page
    """

    def setUp(self):
        self.board = Board.objects.create(name='Django',
                                          description='Django board')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse(
            'board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response,
                            'href="{0}"'.format(board_topics_url))


class BoardTopicsTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')

    def test_board_topics_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_topics_view_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)


class NewTopicsTest(TestCase):
    """docstring for NewTopicsTest"""

    def setUp(self):
        Board.objects.create(name='Django', description='Django Board.')

    def test_new_topic_view_success_status_code(self):
        """
        Navigating to the new topic should return a status code=200
        """
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_topic_view_not_found_status_code(self):
        """
        If the topic does not exist, a 404 should be returned
        """
        url = reverse('new_topic', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_new_topic_url_resolves_new_topic_view(self):
        """
        The new topic url should resolve to the new topic view
        function
        """
        self.fail('Need to write this test')
