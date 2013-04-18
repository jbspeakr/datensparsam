# Datensparsam.de

<<<<<<< HEAD

Datensparsam.de is a tool for German citizen allowing them to create personal application forms
for opt-out their private and personal data at governmental record sections.
=======
Datensparsam.de is a tool for German citizen providing a simple way for German citizen 
to opt-out from governmental record sections by generating personal application forms 
(so-called *Anträge auf Übermittlungssperren*).
>>>>>>> b33e5bfd7136e7d0a47aae2479f137aa49b5891e

This Python- and Django-based civic app was mainly planned and implemented by Jan Brennenstuhl
during the international Open-Data-Day 2013 in Berlin.

## Setup

### Load API Fixtures

    python manage.py loaddata api-municipality
    python manage.py loaddata api-registrationoffice
    python manage.py loaddata api-zipcode
