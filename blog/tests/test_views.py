from django.test import Client
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from blog.views import *


class TestViews(TestCase):

    def test_view_home_page(self):
        response = self.client.get(reverse(home))
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_view_ajout_post_correct_template(self):
        response = self.client.get(reverse(post_create))
        self.assertTemplateUsed(response, 'blog/post_form.html')

    def test_view_ajout_post_with_correct_title(self):
        user = User.objects.create(username="Testeur", email="testin@gmail.com")
        user.set_password("testing321")
        user.save()
        c = Client()
        c.login(username="Testeur",password="testing321")
        c.post('/post/new/', data={'title': 'Test', 'content': 'letest'})
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().title, 'Test')

    def test_view_ajout_post_missing_field(self):
        user = User.objects.create(username="Testeur", email="testin@gmail.com")
        user.set_password("testing321")
        user.save()
        c = Client()
        c.login(username="Testeur", password="testing321")
        c.post('/post/new/', data={'content': 'letest'})
        self.assertEqual(Post.objects.count(), 0)

    def test_redirect_home_after_saving(self):
        user = User.objects.create(username="Testeur", email="testin@gmail.com")
        user.set_password("testing321")
        user.save()
        c = Client()
        c.login(username="Testeur", password="testing321")
        reponse = c.post('/post/new/', data={'title': 'Test', 'content': 'letest'})
        self.assertRedirects(reponse, '/')

    def test_can_save_a_POST(self):
        user = User.objects.create(username="Testeur", email="testin@gmail.com")
        user.set_password("testing321")
        user.save()
        c = Client()
        c.login(username="Testeur", password="testing321")
        c.post('/post/new/', data={'title': 'Title', 'content': 'letest'})
        self.assertEqual(Post.objects.count(),1)
        new_item = Post.objects.first()
        self.assertEqual(new_item.title, 'Title')