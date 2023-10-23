from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class URLTests(TestCase):
    def test_home_url(self):
        self.assertEqual(1,1)
        response = self.client.get(reverse('charts'))
        self.assertEqual(response.status_code, 200)

    def test_other_url(self):
        response = self.client.get(reverse('charts'))
        self.assertTemplateUsed(response, 'blog/charts.html')
        # response = self.client.get(reverse(''))
        # self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'Expected Content')