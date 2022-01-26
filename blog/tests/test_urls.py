from django.urls import reverse, resolve
from blog.views import *
from django.test import TestCase

class TestUrls(TestCase):

    def test_root_url(self):
        found = resolve('/')
        self.assertEqual(found.func, home)

    def test_ajout_post_url_resolve(self):
        found = resolve('/post/new/')
        self.assertEqual(found.func, post_create)

    def test_view_url_exists_at_desired_location(self):
        reponse = self.client.get('/post/new/')
        self.assertEqual(reponse.status_code, 200)

    def test_view_url_accessible_by_name(self):
        reponse = self.client.get(reverse('post-create'))
        self.assertEqual(reponse.status_code, 200)