from django.apps import apps
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from archiv.dal_urls import urlpatterns
from archiv.models import KeyWord, UseCase, Text, Autor, Stelle
from archiv.utils import parse_date, cent_from_year
from archiv.text_processing import process_text
from archiv.nlp_utils import get_nlp_data
from topics.models import StopWord

MODELS = list(apps.all_models["archiv"].values())

client = Client()
USER = {"username": "testuser", "password": "somepassword"}

DATES_DEFAULT = 600

DATES = [["800", 800], ["asfd800? ? ", 800], ["", DATES_DEFAULT]]

CENTURY_TEST_DATA = [
    [0, 1],
    [-1, -1],
    [-40, -1],
    [-101, -2],
    [40, 1],
    [100, 1],
    [101, 2],
    [1000, 10],
    [1001, 11],
]


class ArchivTestCase(TestCase):
    fixtures = ["dump.json"]

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
                response = client.get(url, {"pk": item.id})
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
                response = client.get(url, {"pk": item.id})
                self.assertEqual(response.status_code, 200)

    def test_005_createviews_not_logged_in(self):
        for x in MODELS:
            item = x.objects.first()
            try:
                url = item.get_createview_url()
            except AttributeError:
                url = False
            if url:
                response = client.get(url, {"pk": item.id})
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
                response = client.get(url, {"pk": item.id})
                self.assertEqual(response.status_code, 200)

    def test_007_timetable(self):
        item = UseCase.objects.first()
        url = reverse("archiv:usecase_timetable_json", kwargs={"pk": item.id})
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_008_keyword_data_endpoint(self):
        url = f"{reverse('archiv:keyword_data')}?rvn_stelle_key_word_keyword__text__autor=40"
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_009_centuries(self):
        for x in CENTURY_TEST_DATA:
            self.assertEqual(cent_from_year(x[0]), x[1])

    def test_010_kw_cent_ep(self):
        for x in KeyWord.objects.all():
            url = reverse("archiv:keyword_by_century", kwargs={"pk": x.id})
            response = client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_011_text_tei_view(self):
        for x in Text.objects.all():
            url = x.get_tei_url()
            response = client.get(url, {"pk": x.id})
            self.assertEqual(response.status_code, 200)
            self.assertTrue(f"{x.title}" in response.content.decode())

    def test_012_string_to_dict(self):
        my_text = "De palatio venio Caroli et Carolus fuit mihi locutus"
        processed = process_text(my_text)
        self.assertIsInstance(processed, dict)

    def test_013_nlp_data(self):
        url = reverse("archiv:nlp_data")
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_014_check_stopwords(self):
        text = Text.objects.create()
        stelle = Stelle.objects.create(
            text=text,
            zitat="sarvus De gentis et patriae. Gentis sunt nomina, quae ab antiquo suo semper dirivata sunt genere",
        )
        qs = Stelle.objects.filter(id=stelle.id)
        url = f'{reverse("archiv:nlp_data")}?id={stelle.id}'
        self.assertEqual(get_nlp_data(qs)["token"][0], "saruus")
        response = client.get(url).json()
        self.assertEqual(response["token"][0], "saruus")

        StopWord.objects.get_or_create(word="saruus")
        self.assertEqual(get_nlp_data(qs)["token"][0], "gens")
        response = client.get(url).json()
        self.assertEqual(response["token"][0], "gens")

        StopWord.objects.filter(word="saruus").delete()
        self.assertEqual(get_nlp_data(qs)["token"][0], "saruus")
        response = client.get(url).json()
        self.assertEqual(response["token"][0], "saruus")

        StopWord.objects.get_or_create(word="sarvus")
        self.assertEqual(get_nlp_data(qs)["token"][0], "gens")
        response = client.get(url).json()
        self.assertEqual(response["token"][0], "gens")

        StopWord.objects.filter(word="sarvus").delete()
        self.assertEqual(get_nlp_data(qs)["token"][0], "saruus")
        response = client.get(url).json()
        self.assertEqual(response["token"][0], "saruus")

    def test_015_gnd_normalizer(self):
        gnds = [
            ("", ""),
            ("https://lobid.org/gnd/118965808", "https://d-nb.info/gnd/118965808"),
            ("http://d-nb.info/gnd/118965808", "https://d-nb.info/gnd/118965808"),
        ]
        for x in gnds:
            item = Autor.objects.create()
            item.gnd_id = x[0]
            item.save()
            self.assertEqual(x[1], item.gnd_id)

    def test_016_ac_views(self):
        ns = "archiv-ac"
        for x in urlpatterns:
            url_name = f"{ns}:{x.name}"
            url = f"{reverse(url_name)}?q=hansi"
            response = client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTrue("results" in response.json().keys())
