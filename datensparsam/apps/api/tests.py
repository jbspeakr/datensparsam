import json
from django.test import TestCase
from django.test.client import Client
from datensparsam.apps.api import models


class ApiTest(TestCase):
    fixtures = [
        'api-municipality.json',
        'api-registrationoffice.json',
        'api-zipcode.json',
    ]

    def setUp(self):
        """This method is automatically called by the Django test framework."""
        self.client = Client()

    def get(self, url, status=200):
        """Get a URL and require a specific status code before proceeding"""
        response = self.client.get(url)
        self.assertEqual(response.status_code, status)
        return response

    def test_m2m_sql_access(self):
        zipcode = models.Zipcode.objects.get(id=1)
        municipalities = zipcode.municipalities.all()
        registration_offices = zipcode.registrationoffices.all()

        self.assertTrue(municipalities)
        self.assertTrue(registration_offices)

    def test_m2m_api_access(self):
        url = '/api/v1/zipcode/?format=json'
        response = self.get(url).content
        new_json = json.loads(response.decode('utf8'))

        self.assertTrue(new_json)

        zipcode = new_json['objects'][0]

        self.assertTrue('zipcode' in zipcode)
        self.assertTrue('municipalities' in zipcode)

    def test_municipality_api_access(self):
        url = '/api/v1/municipality/?format=json'
        response = self.get(url).content
        new_json = json.loads(response.decode('utf8'))

        self.assertTrue(new_json)

        municipality = new_json['objects'][0]

        self.assertTrue('city' in municipality)
        self.assertTrue('id' in municipality)
        self.assertTrue('key' in municipality)
        self.assertTrue('lat' in municipality)
        self.assertTrue('lng' in municipality)
        self.assertTrue('name' in municipality)
        self.assertTrue('street' in municipality)
        self.assertTrue('zipcode' in municipality)

    def test_registrationoffice_api_access(self):
        url = '/api/v1/registration-office/?format=json'
        response = self.get(url).content
        new_json = json.loads(response.decode('utf8'))

        self.assertTrue(new_json)

        municipality = new_json['objects'][0]

        self.assertTrue('city' in municipality)
        self.assertTrue('id' in municipality)
        self.assertTrue('lat' in municipality)
        self.assertTrue('lng' in municipality)
        self.assertTrue('name' in municipality)
        self.assertTrue('street' in municipality)
        self.assertTrue('zipcode' in municipality)
