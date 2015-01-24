# Datensparsam.de

[![Build Status](https://api.travis-ci.org/jbspeakr/datensparsam.svg?branch=master)](https://travis-ci.org/jbspeakr/datensparsam)
[![Coverage Status](https://img.shields.io/coveralls/jbspeakr/datensparsam.svg?branch=master)](https://coveralls.io/r/jbspeakr/datensparsam)
[![Codacy Badge](https://www.codacy.com/project/badge/8231e85ef0704c32834d437e9246311d)](https://www.codacy.com/public/jbspeakr/datensparsam.git)

Datensparsam.de is a tool for German citizen providing a simple way for German citizen
to opt-out from governmental record sections by generating personal application forms
(so-called *Anträge auf Übermittlungssperren*).

This Python- and Django-based civic app was mainly planned and implemented by Jan Brennenstuhl
during the international Open-Data-Day 2013 in Berlin.

## Setup

### Load API Fixtures

    python manage.py loaddata api-municipality
    python manage.py loaddata api-registrationoffice
    python manage.py loaddata api-zipcode

### Load PDF-Builder Fixture

    python manage.py loaddata pdfbuilder-form
