from django.apps import apps
from django.test import TestCase, Client

from archiv.models import KeyWord

MODELS = list(apps.all_models['archiv'].values())
client = Client()


class ArchivTestCase(TestCase):
    fixtures = ['dump.json']

    def test_001_source(self):
        # A test that uses the fixtures.
        items = KeyWord.objects.all()
        self.assertTrue(items.count() > 1, 1)

    def test_002_listviews(self):
        for x in MODELS:
            try:
                url = x.get_listview_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url)
                self.assertEqual(response.status_code, 200)

    def test_003_detailviews(self):
        for x in MODELS:
            item = x.objects.first()
            try:
                url = item.get_absolute_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {'pk': item.id})
                self.assertEqual(response.status_code, 200)
