from django.test import TestCase, Client
from django.urls import reverse
from django.conf import settings
from generic_ac.urls import urlpatterns


client = Client()

API_ROOT = "/api/?format=json"
GN_AC_NS = "generic-ac"
GN_AC_CONF = settings.GENERIC_AC_CONFIG


class ApiTestCase(TestCase):
    fixtures = ["dump.json"]

    def test_001_api_endpoint(self):
        r = client.get(API_ROOT)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.accepted_media_type, "application/json")

    def test_002_model_endpoints(self):
        endpoints = client.get(API_ROOT).json()
        for _, value in endpoints.items():
            r = client.get(value)
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.accepted_media_type, "application/json")

    def test_003_generic_ac(self):
        for x in urlpatterns:
            url_name = f"{GN_AC_NS}:{x.name}"
            url = f"{reverse(url_name)}?q=obi"
            response = client.get(url)
            self.assertEqual(response.status_code, 200)

    def test_004_generic_ac_only_those(self):
        url_name = f"{GN_AC_NS}:describe"
        url = f"{reverse(url_name)}"
        response = client.get(url)
        self.assertEqual(response.json(), GN_AC_CONF)
        self.assertEqual(response.status_code, 200)

    def test_005_generic_ac_only_those(self):
        url_name = f"{GN_AC_NS}:generic_ac"
        url = f"{reverse(url_name)}?kind=autor&limit=100&page=1"
        response = client.get(url)
        authors = int(response.json()["count"])
        url = f"{reverse(url_name)}?limit=100"
        response = client.get(url)
        all_kinds = int(response.json()["count"])
        self.assertTrue(authors < all_kinds)
        url = f"{reverse(url_name)}?limit=1"
        response = client.get(url)
        self.assertTrue(response.json()["next"])
        url = f"{reverse(url_name)}?limit=1&page=2"
        response = client.get(url)
        self.assertTrue(response.json()["previous"])
        url = f"{reverse(url_name)}?limit=1&page=2&q=sadlfjsalöfjlsdafjsdlkfj"
        response = client.get(url)
        self.assertEqual(int(response.json()["count"]), 0)
        url = f"{reverse(url_name)}?limit=hansi&page=sumsi"
        response = client.get(url)
        self.assertTrue(int(response.json()["count"]))
