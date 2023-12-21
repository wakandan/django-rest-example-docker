from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from django.core.cache import cache
from django.conf import settings

# Create your tests here.


class TestDummy(TestCase):
    def test_value(self):
        self.assertEqual(1, 1)


class TestSearchView(APITestCase):
    fixtures = ["rest_example/tests/fixtures/employees.json"]

    def setUp(self) -> None:
        self.url = reverse("search")
        self.client = APIClient()
        cache.clear()

    def test_search_api_by_status(self):
        response = self.client.get(self.url, data={"status": "ACTIVE"})
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertEqual(3, len(response_json))

    def test_search_api_by_position(self):
        response = self.client.get(self.url, data={"position": "ASSISTANT_MANAGER"})
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertEqual(1, len(response_json))

    def test_search_api_by_invalid_position(self):
        response = self.client.get(self.url, data={"position": "INVALID_POSITION"})
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertEqual(0, len(response_json))

    def test_search_api_by_location(self):
        response = self.client.get(self.url, data={"location": "HO_CHI_MINH"})
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertEqual(1, len(response_json))

    def test_search_api_by_department(self):
        response = self.client.get(self.url, data={"department": "IT"})
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertEqual(1, len(response_json))

    def test_search_api_by_company(self):
        response = self.client.get(self.url, data={"company": "NTUC"})
        self.assertEqual(response.status_code, 200)
        response_json = response.json()
        self.assertEqual(2, len(response_json))


class TestRateLimiter(TestCase):
    def setUp(self) -> None:
        self.url = reverse("search")
        self.client = APIClient()

    def test_rate_limiter(self):
        for i in range(settings.RATE_LIMITER_MAX_REQUESTS_PER_MIN + 10):
            response = self.client.get(self.url)
            if i > settings.RATE_LIMITER_MAX_REQUESTS_PER_MIN:
                self.assertEqual(403, response.status_code)
