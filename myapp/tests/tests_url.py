from django.test import SimpleTestCase
from django.urls import reverse, resolve
from myapp.views import index, upload 




class TestUrls(SimpleTestCase):

    """
        This is to test the all URLs inside our app.
    """

    def test_index_url_resolve(self):
        """
        This is to test the homepage URL
        """
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)


    def test_fileUplaod_url_resolve(self):
        """
        This is to test the upload URL
        """
        url = reverse('upload')
        self.assertEqual(resolve(url).func, upload)