from django.apps import apps
from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from archiv.crud_registry import crud
from archiv.dal_urls import urlpatterns
from archiv.models import Autor, KeyWord, Text, UseCase
from archiv.utils import cent_from_year, parse_date

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

    def test_013_nlp_data(self):
        url = reverse("archiv:nlp_data")
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

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
            self.assertTrue("results" in response.json())

    def test_017_crud_views_anonymous(self):
        for model in crud._registry:
            base = model._get_url_basename()
            item = model.objects.first() or model.objects.create()
            public = {
                "browse": reverse(f"archiv:{base}_browse"),
                "detail": reverse(f"archiv:{base}_detail", kwargs={"pk": item.id}),
            }
            for action, url in public.items():
                with self.subTest(model=model.__name__, action=action):
                    self.assertEqual(client.get(url).status_code, 200)
            protected = {
                "create": reverse(f"archiv:{base}_create"),
                "edit": reverse(f"archiv:{base}_edit", kwargs={"pk": item.id}),
                "delete": reverse(f"archiv:{base}_delete", kwargs={"pk": item.id}),
            }
            for action, url in protected.items():
                with self.subTest(model=model.__name__, action=action):
                    self.assertEqual(client.get(url).status_code, 302)

    def test_018_crud_views_logged_in(self):
        self.client.login(**USER)
        for model in crud._registry:
            base = model._get_url_basename()
            item = model.objects.first() or model.objects.create()
            urls = {
                "create": reverse(f"archiv:{base}_create"),
                "edit": reverse(f"archiv:{base}_edit", kwargs={"pk": item.id}),
                "delete": reverse(f"archiv:{base}_delete", kwargs={"pk": item.id}),
            }
            for action, url in urls.items():
                with self.subTest(model=model.__name__, action=action):
                    self.assertEqual(self.client.get(url).status_code, 200)

    def test_019_endpoints(self):
        for name in ["keyword_stelle", "stopwords", "keyword_data"]:
            with self.subTest(name=name):
                response = client.get(reverse(f"archiv:{name}"))
                self.assertEqual(response.status_code, 200)
