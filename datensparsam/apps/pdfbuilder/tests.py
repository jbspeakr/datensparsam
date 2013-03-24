#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test.client import Client

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


class PdfCreationTest(TestCase):
    fixtures = [
        'pdfbuilder-form.json',
        'pdfbuilder-municipality.json',
        'pdfbuilder-recordsection.json',
        'pdfbuilder-zipcode.json'
    ]

    def setUp(self):
        """This method is automatically called by the Django test framework."""
        self.client = Client()

    def POST(self, url, params, status=200, mimetype="application/pdf"):
        """Make a POST and require a specific status code before proceeding"""
        response = self.client.post(url, params)
        self.failUnlessEqual(response.status_code, status)
        # self.failUnless(response.headers['Content-Type'].startswith(mimetype))
        return response

    def GET(self, url, status=200, mimetype="text/html"):
        """Get a URL and require a specific status code before proceeding"""
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, status)
        # self.failUnless(response.headers['Content-Type'].startswith(mimetype))
        return response

    def test_former_errors(self):
        params = [{
            'zipcode': '45529',
            'state': '10',
        }, {
            'zipcode': '66123',
            'state': '12',
        }, {
            'zipcode': '80634',
            'state': '2',
        }, {
            'zipcode': '70178',
            'state': '1',
        }, {
            'zipcode': '01465',
            'state': '14',
        }, {
            'zipcode': '40489',
            'state': '10',
        }, {
            'zipcode': '40235',
            'state': '10',
        }, {
            'zipcode': '24111',
            'state': '15',
        }, {
            'zipcode': '70439',
            'state': '1',
        }, {
            'zipcode': '60318',
            'state': '7',
        }, {
            'zipcode': '12051',
            'state': '3',
        }, {
            'zipcode': '65187',
            'state': '7',
        }, {
            'zipcode': '53115',
            'state': '10',
        }, {
            'zipcode': '38448',
            'state': '9',
        }, {
            'zipcode': '22765',
            'state': '6',
        }, {
            'zipcode': '14482',
            'state': '4',
        }]
        for param in params:
            param['city'] = param['name'] = param['firstname'] = param['address'] = 'Test'
            self.POST('/', param)
