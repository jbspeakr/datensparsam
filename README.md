# Datensparsam

[![Build Status](https://api.travis-ci.org/jbspeakr/datensparsam.svg?branch=master)](https://travis-ci.org/jbspeakr/datensparsam)
[![Coverage Status](https://coveralls.io/repos/jbspeakr/datensparsam/badge.svg?branch=master)](https://coveralls.io/r/jbspeakr/datensparsam?branch=master)
[![Codacy Badge](https://www.codacy.com/project/badge/8231e85ef0704c32834d437e9246311d)](https://www.codacy.com/public/jbspeakr/datensparsam.git)
[![Deployment status from dploy.io](https://jbspeakr.dploy.io/badge/23779029953300/19361.png)](http://dploy.io)

**[Datensparsam.de](https://www.datensparsam.de) is a Privacy Empowerment App written in Python using Flask 0.10.1.**

It provides a simple way for German citizen to opt-out from local residents' registration offices by generating personal 
application forms (so-called *Anträge auf Übermittlungssperren*).

This civic app was mainly planned and implemented by [Jan Brennenstuhl](http://jan.brennenstuhl.me) during the international Open-Data-Day 2013 in Berlin.

## How do I use it?

1. edit the configuration in the datensparsam.py file or 
   export an FLASKR_SETTINGS environment variable pointing to a configuration file.
2. initialize the database with this command:
        
        tbc.

3. now you can run flaskr:

         python manage.py runserver

the application will greet you on http://localhost:5000/
## Any Test?

You betcha. Run'em using:  
        
        nosetests
    
## What do I need?
    
[![Requirements Status](https://requires.io/github/jbspeakr/datensparsam/requirements.svg?branch=master)](https://requires.io/github/jbspeakr/datensparsam/requirements/?branch=master)

