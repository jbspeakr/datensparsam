# Datensparsam

[![Build Status](https://api.travis-ci.org/jbspeakr/datensparsam.svg?branch=master)](https://travis-ci.org/jbspeakr/datensparsam)
[![Coverage Status](https://coveralls.io/repos/jbspeakr/datensparsam/badge.svg?branch=master)](https://coveralls.io/r/jbspeakr/datensparsam?branch=master)
[![Codacy Badge](https://www.codacy.com/project/badge/8231e85ef0704c32834d437e9246311d)](https://www.codacy.com/public/jbspeakr/datensparsam.git)
[![Deployment status from dploy.io](https://jbspeakr.dploy.io/badge/23779029953300/19361.png)](http://dploy.io)

**[Datensparsam.de](https://www.datensparsam.de) is a Privacy Empowerment App written in Python using Django.**

It provides a simple way for German citizen to opt-out from local residents' registration offices by generating personal 
application forms (so-called *Anträge auf Übermittlungssperren*).

This civic app was mainly planned and implemented by [Jan Brennenstuhl](http://jan.brennenstuhl.me) during the international Open-Data-Day 2013 in Berlin.
    
## What do I need?
    
[![Requirements Status](https://requires.io/github/jbspeakr/datensparsam/requirements.svg?branch=master)](https://requires.io/github/jbspeakr/datensparsam/requirements/?branch=master)

## How do I use it?

1. initialize the database:
        
        python manage.py migrate

2. fill database with fixtures:

        python manage.py loaddata api-municipality
        python manage.py loaddata api-registrationoffice
        python manage.py loaddata api-zipcode
        python manage.py loaddata pdfbuilder-form

3. now you can run the server:

         python manage.py runserver

## Any Test?

You betcha. Run'em using:  
        
        python manage.py test --failfast