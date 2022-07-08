from django.test import TestCase, Client
from posts.models import User, Post, Group


class ImageTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="Paul", email="paul@beatles.ru", password="12345")
        self.group = Group.objects.create(title='test-group', slug='test-link', description='Тестовое описание группы')
        self.post = Post.objects.create(text='im', author=self.user)
        self.client.login(username="Paul", password="12345")

    def image_in_post(self):
        with open('media/posts/0679412251_6_1_1.jpg', 'rb') as img:
            post = self.client.post('/Paul/1/edit/', {'author': self.user, 'text': 'post with image',
                                                      'image': img},
                                    follow=True)
        response = self.client.get('/Paul/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('<img' in response.content.decode())
        self.assertEqual(response.context['post'].image, post.context['post'].image)

        response = self.client.get('/Paul')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('<img' in response.content.decode())

        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('<img' in response.content.decode())

    def image_in_group_post(self):
        with open('media/posts/0679412251_6_1_1.jpg', 'rb') as img:
            post = self.client.post('/Paul/1/edit/', {'author': self.user, 'text': 'post with image',
                                                      'image': img, 'group': self.group},
                                    follow=True)
        response = self.client.get('/group/test-link/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('<img', response.content.decode())
