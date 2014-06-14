from distutils.core import setup

setup(
    name='datensparsam',
    version='0.4',
    packages=['datensparsam', 'datensparsam.apps', 'datensparsam.apps.api', 'datensparsam.apps.pdfbuilder',
              'datensparsam.apps.pdfbuilder.forms'],
    url='https://www.datensparsam.de',
    license='MIT License',
    author='Jan Brennenstuhl',
    author_email='jan@brennenstuhl.me',
    description='Django-based civic app to opt-out at governmental record sections.'
)
