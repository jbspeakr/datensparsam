# -*- coding: utf-8 -*-
"""
    datensparsam.municipality.models
    ~~~~~~~~~~~~~~~~~~~~~~
    Municipality models.
"""
from mongoengine import Document, StringField, IntField


class Municipality(Document):
    """
    "city": "Pr\u00fcm",
    "name": "Verbandsgemeindeverwaltung Pr\u00fcm",
    "zipcode": "54595",
    "state": "Rheinland-Pfalz",
    "street": "Tiergartenstr. 54",
    "key": "07232227"
    """
    city = StringField(max_length=120, required=True)
    name = StringField(max_length=120, required=True)
    zipcode = IntField(max_length=120, required=True)
    state = StringField(max_length=6, required=True)
    street = StringField(max_length=120, required=True)
    key = IntField(max_length=10, required=True)


