# -*- coding: utf-8 -*-
import os
from flask.ext.script import Manager
from datensparsam import create_app


manager = Manager(create_app)
manager.add_option('-c', '--config', dest='config', required=False)

if __name__ == '__main__':
    os.environ.setdefault('DATENSPARSAM_SETTINGS', 'settings.development')
    manager.run()