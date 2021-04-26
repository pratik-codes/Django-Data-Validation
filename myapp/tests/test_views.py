from django.test import RequestFactory
from django.urls import reverse
from myapp.views import index, upload


class TestViews:
    """
        This is to test the views inside our app.
    """

    def test_index_homepage(self):
        """
            This is to test the homepage views inside our app.
        """
        path = reverse('')
        #creating request
        request = RequestFactory().get(path)
        # testing the reponse if it comes out to be 200 
        response = index(request)
        assert response.status_code == 200

    def test_upload(self):
        """
            This is to test the file upload views inside our app.
        """
        path = reverse('')
        #creating request
        request = RequestFactory().post(path)
        # testing the reponse if it comes out to be 200 
        response = index(request)
        assert response.status_code == 200