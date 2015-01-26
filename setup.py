from distutils.core import setup

setup(
    name='datensparsam',
    version='0.5',
    packages=['dtnsprsm', 'dtnsprsm.apps', 'dtnsprsm.apps.api', 'dtnsprsm.apps.pdfbuilder',
              'dtnsprsm.apps.pdfbuilder.forms'],
    url='https://www.datensparsam.de',
    license='MIT License',
    author='Jan Brennenstuhl',
    author_email='jan@brennenstuhl.me',
    description='Django-based civic app to opt-out at governmental record sections.'
)
