from django.test import TestCase, Client
from django.urls import reverse

from posts.models import User, Post, Group


class ProfileTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="Paul", email="paul@beatles.ru", password="12345")
        self.post = Post.objects.create(text='Help!', author=self.user)

    def test_profile(self):
        response = self.client.get('/Paul')
        self.assertEqual(response.status_code, 200)

    def test_new_post(self):
        response = self.client.get('/new/')
        self.assertEqual(response.status_code, 200)

    def test_not_get_new_post(self):
        c = Client()
        response = c.get('/new/', follow=True)
        self.assertRedirects(response, '/auth/login/')

    def test_new_post_get(self):
        response = self.client.get('')
        self.assertIn(str(self.post), response.content.decode())
        response = self.client.get('/Paul')
        self.assertIn(str(self.post), response.content.decode())
        response = self.client.get('/Paul/1/')
        self.assertIn(str(self.post), response.content.decode())

    def test_post_edit(self):
        status = self.client.post('/Paul/1/edit/', kwargs={'pk': self.post.pk, 'author': self.user},
                                  data={'text': 'Help!!', 'author': self.user})
        new_post = Post.objects.filter(pk=self.post.pk)
        self.assertIn('Help!!', new_post)
