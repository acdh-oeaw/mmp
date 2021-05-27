from django.test import TestCase

from archiv.models import KeyWord


class ArchivTestCase(TestCase):
    fixtures = ['dump.json']

    def test_001_source(self):
        # A test that uses the fixtures.
        items = KeyWord.objects.all()
        self.assertTrue(items.count() > 1, 1)
