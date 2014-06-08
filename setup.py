import os
from setuptools import setup
import codecs
import re
from os import path


README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def read(*parts):
    file_path = path.join(path.dirname(__file__), *parts)
    return codecs.open(file_path).read()

setup(
    name='datensparsam',
    version='0.3',
    packages=['datensparsam'],
    license='MIT License',
    description='Django-based civic app to opt-out at governmental record sections',
    long_description=read('README.md'),
    url='https://www.datensparsam.de',
    author='Jan Brennenstuhl',
    author_email='jan@brennenstuhl.me',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
