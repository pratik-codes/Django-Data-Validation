from django.test import SimpleTestCase
from django.urls import reverse, resolve
from myapp.views import index, upload 




class TestUrls(SimpleTestCase):

    def test_index_url_resolve(self):
        url = reverse('index')
        print(url)
        self.assertEqual(resolve(url).func, index)


    def test_fileUplaod_url_resolve(self):
        url = reverse('upload')
        print(url)
        self.assertEqual(resolve(url).func, upload)