#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.test import TestCase

from datensparsam.apps.pdfbuilder.models import Municipality
from datensparsam.apps.pdfbuilder.models import Recordsection


class FixtureTest(TestCase):
    def test_query_recordsection(self):
        create_recordsection()
        queryset = Recordsection.objects.filter(municipality='6531013')

        for recordsection in queryset:
            self.assertEqual(recordsection.zipcode, '35457')


def create_recordsection():
    """
    Creates a municipality and the corresponding recordsection with ...
    """
    municipality = create_municipality()
    return Recordsection.objects.create(
        municipality=municipality,
        address=u'Magistrat der Stadt Lollar',
        city=u'Lollar',
        zipcode=u'35457',
        street=u'Holzmühler Weg 76'
        )


def create_municipality():
    """
    Creates a municipality with ...
    """
    return Municipality.objects.create(
        key=u'6531013',
        kind=u'Stadt',
        district=u'Reg.-Bez. Gießen',
        zipcode=u'35457',
        state=u'Hessen',
        name=u'Lollar, Stadt',
        county=u'Gießen'
        )
