from distutils.core import setup
from pip.req import parse_requirements

requirements = parse_requirements('requirements.txt')
requirements_list = [str(ir.req) for ir in requirements]

setup(
    name='datensparsam',
    version='1.0',
    packages=['datensparsam'],
    url='https://www.datensparsam.de',
    license='MIT License',
    author='Jan Brennenstuhl',
    author_email='jan@brennenstuhl.me',
    description='Python-based civic app to opt-out at governmental record sections.',
    long_description=open('README.md').read() + '\n\n' + open('CHANGES.md').read(),
    install_requires=requirements_list
)
