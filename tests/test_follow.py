from django.test import TestCase, Client
from posts.models import User, Follow, Post


class FollowTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create_user(username="Paul", email="paul@beatles.ru", password="12345")
        self.user2 = User.objects.create_user(username='Ringo', email='ringo@beatles.ru', password="12345")
        self.user3 = User.objects.create_user(username='John', email='john@beatles.ru', password="12345")
        self.post1 = Post.objects.create(text='Yesterday', author=self.user1)
        self.post2 = Post.objects.create(text='Help!', author=self.user2)
        self.client.login(username="Paul", password="12345")

    def profile_follow_test(self):
        response = self.client.get('/Ringo/follow/', follow=True)
        self.assertEqual(response.status_code, 200)
        following = Follow.objects.get(pk=1)
        self.assertTrue(following)

    def profile_unfollow_test(self):
        response = self.client.get('/Ringo/follow/', follow=True)
        response = self.client.get('/Ringo/unfollow/', follow=True)
        following = Follow.objects.all()
        self.assertEqual(len(following), 0)

    def get_post_in_follow_index_test(self):
        response = self.client.get('/Ringo/follow/', follow=True)
        response = self.client.get('/follow/')
        self.assertTrue('Help!' in response.content.decode())

    def not_get_post_in_follow_index_test(self):
        self.client.login(username="John", password="12345")
        response = self.client.get('/Paul/follow/', follow=True)
        response = self.client.get('/follow/')
        self.assertFalse('Help!' in response.content.decode())

    def add_comment_if_authenticated_test(self):
        comment = self.client.post('/Ringo/2/comment/', {'text': 'Hey', 'author': self.user1}, follow=True)
        response = self.client.get('/Ringo/2/')
        self.assertTrue('Hey' in response.content.decode())

    def add_comment_if_not_authenticated_test(self):
        c = Client()
        comment = c.post('/Ringo/2/comment/', {'text': 'Hey', 'author': self.user1}, follow=True)
        response = self.client.get('/Ringo/2/')
        self.assertFalse('Hey' in response.content.decode())
