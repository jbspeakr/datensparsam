# -*- coding: utf-8 -*-
import os
from flask import Flask
from .api.municipality import blueprint as municipality_blueprint


def create_app(config=None):
    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(os.environ.get('DATENSPARAM_SETTINGS'))

    for part in [municipality_blueprint]:
        app.register_blueprint(part)

    return app
