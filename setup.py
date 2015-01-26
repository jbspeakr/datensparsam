from distutils.core import setup
import codecs
import os


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()

setup(
    name='datensparsam',
    version='0.5',
    packages=['dtnsprsm', 'dtnsprsm.apps', 'dtnsprsm.apps.api', 'dtnsprsm.apps.pdfbuilder',
              'dtnsprsm.apps.pdfbuilder.forms'],
    url='https://www.datensparsam.de',
    license='MIT License',
    author='Jan Brennenstuhl',
    author_email='jan@brennenstuhl.me',
    description='A Privacy Empowerment App for German citizen written in Python using Django.',
    long_description=read('README.md')
)
