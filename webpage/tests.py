from django.http import Http404
from django.test import TestCase

from webpage.views import GenericWebpageView


class WebpageTest(TestCase):
    def test_webpage(self):
        rv = self.client.get("/")
        self.assertEqual(rv.status_code, 200)

    def test_missing_template_returns_404(self):
        view = GenericWebpageView()
        view.kwargs = {"template": "missing-page"}
        with self.assertRaises(Http404):
            view.get_template_names()
