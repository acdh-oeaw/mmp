from django.test import TestCase, Client


client = Client()

API_ROOT = '/api/?format=json'


class ApiTestCase(TestCase):
    fixtures = ["dump.json"]

    def test_001_api_endpoint(self):
        r = client.get(API_ROOT)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.accepted_media_type, 'application/json')

    def test_002_model_endpoints(self):
        endpoints = client.get(API_ROOT).json()
        for _, value in endpoints.items():
            r = client.get(value)
            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.accepted_media_type, 'application/json')
