#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse


class PdfBuilderTest(TestCase):

    fixtures = [
        'pdfbuilder-form.json',
        'api-municipality.json',
        'api-registrationoffice.json',
    ]

    def setUp(self):
        """This method is automatically called by the Django test framework."""
        self.client = Client()

    def POST(self, url, params, status=200):
        """Make a POST and require a specific status code before proceeding"""
        response = self.client.post(url, params)
        self.failUnlessEqual(response.status_code, status)
        return response

    def test_pdf_creation(self):
        '''  '''
        params = {
            'name': 'Nachname',
            'firstname': 'Vorname',
            'address': 'Teststr. 1',
            'zipcode': '12345',
            'city': 'Stadt',
            'registrationoffice': '1629',
            'municipality': '15',
        }
        self.POST(reverse('pdfbuilder-pdf'), params)
