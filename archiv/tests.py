from django.apps import apps
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from archiv.models import KeyWord, UseCase
from archiv.utils import parse_date

MODELS = list(apps.all_models['archiv'].values())

client = Client()
USER = {
    "username": "testuser",
    "password": "somepassword"
}

DATES_DEFAULT = 600

DATES = [
    ['800', 800],
    ['asfd800? ? ', 800],
    ['', DATES_DEFAULT]
]


class ArchivTestCase(TestCase):
    fixtures = ['dump.json']

    def setUp(self):
        # Create two users
        User.objects.create_user(**USER)

    def test_parse_date(self):
        for x in DATES:
            parsed = parse_date(x[0], default=DATES_DEFAULT)
            self.assertEqual(parsed, x[1])

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

    def test_004_editviews(self):
        client.login(**USER)
        for x in MODELS:
            item = x.objects.first()
            try:
                url = item.get_edit_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {'pk': item.id})
                self.assertEqual(response.status_code, 200)

    def test_005_createviews_not_logged_in(self):
        for x in MODELS:
            item = x.objects.first()
            try:
                url = item.get_createview_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {'pk': item.id})
                self.assertEqual(response.status_code, 302)

    def test_006_createviews_logged_in(self):
        client.login(**USER)
        for x in MODELS:
            item = x.objects.first()
            try:
                url = item.get_createview_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {'pk': item.id})
                self.assertEqual(response.status_code, 200)

    def test_007_timetable(self):
        item = UseCase.objects.first()
        url = reverse('archiv:usecase_timetable_json', kwargs={'pk': item.id})
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_008_keyword_data_endpoint(self):
        url = f"{reverse('archiv:keyword_data')}?rvn_stelle_key_word_keyword__text__autor=40"
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
