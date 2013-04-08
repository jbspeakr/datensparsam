# Datensparsam.de


Datensparsam.de is a tool for German citizen allowing them to create personal application forms
for opt-out their private and personal data at governmental record sections.

This Python- and Django-based civic app was mainly planned and implemented by Jan Brennenstuhl
during the international Open-Data-Day 2013 in Berlin.

## Setup

### Load API Fixtures

    python manage.py loaddata api-municipality
    python manage.py loaddata api-registrationoffice
    python manage.py loaddata api-zipcode
