# -*- coding: utf-8 -*-

"""
    Datensparsam
    ~~~~~~~~~~~~
    A Privacy Empowerment App written in Python
    :copyright: (c) 2015 by Jan Brennenstuhl.
    :license: MIT, see LICENSE.md for more details.
"""

from flask import url_for
from flask.ext.testing import TestCase
from datensparsam import create_app


class MunicipalityApiTest(TestCase):

    def create_app(self):
        app = create_app()
        return app

    def test_api_ping(self):
        res = self.client.get(url_for('municipality.ping'))
        assert res.json == {'ping': 'pong'}
        assert res.status_code == 200