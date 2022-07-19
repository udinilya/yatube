from django.test import TestCase, Client
from posts.models import User, Post


class CacheTest(TestCase):
    def test_index_cache(self):
        self.client = Client()
        self.user = User.objects.create_user(username="Paul", email="paul@beatles.ru", password="12345")
        self.post = Post.objects.create(text='Help!', author=self.user)
        with self.assertNumQueries(5):
            response = self.client.get('')
            response = self.client.get('')
