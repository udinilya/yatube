from django.test import TestCase, Client


class ErrorTest(TestCase):
    def test_error_404(self):
        c = Client()
        response = c.get('/end')
        self.assertEqual(response.status_code, 404)
