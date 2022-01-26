from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import Post


class TestModelsBlog(TestCase):

    def test_add_2_posts(self):
        user = User.objects.create(username="Testeur", password="testing321", email="testeur@gmail.com")

        blog_first = Post()
        blog_first.title = 'First'
        blog_first.content = 'ContenuFirst'
        blog_first.author = user

        blog_second = Post()
        blog_second.title = 'Second'
        blog_second.content = 'ContenuSecond'
        blog_second.author = user

        blog_first.save()
        blog_second.save()

        self.assertEqual(Post.objects.count(), 2)

    def test_hasattr_content(self):
        self.assertTrue(hasattr(Post(), 'content'))

    def test_attribute_modele_saved(self):
        a = Post.objects.create(title='Test', content='ContenuTest')
        self.assertEqual(a.title, 'Test')

    def test_attr_modele_is_too_long(self):
        a = Post.objects.create(title='Test' * 101, content='ContenuTest')
        with self.assertRaises(ValidationError):
            a.full_clean()

