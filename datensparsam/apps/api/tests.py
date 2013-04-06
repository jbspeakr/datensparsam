"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

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

    def GET(self, url, status=200, mimetype="application/json"):
        """Get a URL and require a specific status code before proceeding"""
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, status)
        return response

    def test_plain_sql_access(self):
        zipcode = models.Zipcode.objects.get(id=1)
        municipalities = zipcode.municipalities.all()
        registration_offices = zipcode.registration_offices.all()

        self.assertTrue(municipalities)
        self.assertTrue(registration_offices)

    def test_json_api_access(self):
        url = '/api/v1/zipcode/?format=json'
        response = self.GET(url)
        newJson = json.loads(response.content, encoding='utf-8')

        self.assertTrue(newJson)

        zipcode = newJson['objects'][0]
        print zipcode

        self.assertTrue('zipcode' in zipcode)
        self.assertTrue('municipalities' in zipcode)
