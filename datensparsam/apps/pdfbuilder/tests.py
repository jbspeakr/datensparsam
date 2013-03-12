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

    def test_city_equals_state(self):
        params = {
            'zipcode': '12051',
            'state': '3',
            'city': 'Berlin',
            'name': 'One',
            'firstname': 'Testuser',
            'address': 'Teststreet 1'
        }
        self.POST('/', params)

    def test_multiple_cities(self):
        params = {
            'zipcode': '60318',
            'state': '7',
            'city': 'Frankfurt',
            'name': 'One',
            'firstname': 'Testuser',
            'address': 'Teststreet 1'
        }
        self.POST('/', params)



    def test_non_existing_city(self):
        params = {
            'zipcode': '45529',
            'state': '10',
            'city': 'Test',
            'name': 'One',
            'firstname': 'Testuser',
            'address': 'Teststreet 1'
        }
        self.POST('/', params, status=404)

# class FixtureTest(TestCase):
#     def test_query_recordsection(self):
#         create_recordsection()
#         queryset = Recordsection.objects.filter(municipality='6531013')

#         for recordsection in queryset:
#             self.assertEqual(recordsection.zipcode, '35457')


# def create_recordsection():
#     """
#     Creates a municipality and the corresponding recordsection with ...
#     """
#     municipality = create_municipality()
#     return Recordsection.objects.create(
#         municipality=municipality,
#         address=u'Magistrat der Stadt Lollar',
#         city=u'Lollar',
#         zipcode=u'35457',
#         street=u'Holzmühler Weg 76'
#     )


# def create_municipality():
#     """
#     Creates a municipality with ...
#     """
#     return Municipality.objects.create(
#         key=u'6531013',
#         kind=u'Stadt',
#         district=u'Reg.-Bez. Gießen',
#         zipcode=u'35457',
#         state=u'Hessen',
#         name=u'Lollar, Stadt',
#         county=u'Gießen'
#     )
