from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

# Create your tests here.


class TestDummy(TestCase):
    def test_value(self):
        self.assertEqual(1, 1)


class TestSearchView(APITestCase):
    def setUp(self) -> None:
        self.url = reverse("search")
        self.client = APIClient()

    def test_search_api(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
