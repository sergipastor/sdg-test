from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Country


class CountryAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('countries')

    def test_get_countries_empty(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_post_new_country(self):
        country_name = "Portugal"
        response = self.client.post(self.url, data={"name": country_name}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Country.objects.count(), 1)
        self.assertEqual(response.data['name'], country_name)

    def test_post_existing_country(self):
        country_name = "Italy"
        self.client.post(self.url, {"name": country_name}, format='json')
        
        response = self.client.post(self.url, data={"name": country_name}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Country.objects.count(), 1)

    def test_post_invalid_country(self):
        response = self.client.post(self.url, data={"name": "Made up country"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)
