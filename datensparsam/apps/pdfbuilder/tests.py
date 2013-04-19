#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

# from datensparsam.apps.pdfbuilder.models import Municipality
# from datensparsam.apps.pdfbuilder.models import Recordsection


'''
<option value="1">Baden-Württemberg</option>
<option value="2">Bayern</option>
<option value="3">Berlin</option>
<option value="4">Brandenburg</option>
<option value="5">Bremen</option>
<option value="6">Hamburg</option>
<option value="7">Hessen</option>
<option value="8">Mecklenburg-Vorpommern</option>
<option value="9">Niedersachsen</option>
<option value="10">Nordrhein-Westfalen</option>
<option value="11">Rheinland-Pfalz</option>
<option value="12">Saarland</option>
<option value="13">Sachsen-Anhalt</option>
<option value="14">Sachsen</option>
<option value="15">Schleswig-Holstein</option>
<option value="16">Thüringen</option>
'''


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
