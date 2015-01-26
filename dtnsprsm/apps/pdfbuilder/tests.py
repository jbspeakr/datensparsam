#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

from dtnsprsm.apps.pdfbuilder.models import Form


class PdfBuilderTest(TestCase):

    fixtures = [
        'pdfbuilder-form.json',
        'api-municipality.json',
        'api-registrationoffice.json',
    ]

    def setUp(self):
        """This method is automatically called by the Django test framework."""
        self.client = Client()

    def post(self, url, params, status=200):
        """Make a POST and require a specific status code before proceeding"""
        response = self.client.post(url, params)
        self.assertEqual(response.status_code, status)
        return response

    def test_post_bound_pdf_request(self):
        params = {
            'name': 'Nachname',
            'firstname': 'Vorname',
            'address': 'Teststr. 1',
            'zipcode': '12345',
            'city': 'Stadt',
            'registrationoffice': '1629',
            'municipality': '15'
        }

        self.post(reverse('pdfbuilder-generator'), params, 302)

    def test_empty_content(self):
        self.form = Form.objects.create(
            state='Berlin',
            heading='Widerspruch zur Daten\u00fcbermittlung')
        self.assertFalse(self.form.get_content())