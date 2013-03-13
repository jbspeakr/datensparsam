#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models


class Municipality(models.Model):
    ''' Gemeinde '''
    key = models.CharField(max_length=16, primary_key=True)  # Gemeindeschlüssel
    kind = models.CharField(max_length=48)  # Gemeindetyp
    district = models.CharField(max_length=48)  # Regierungsbezirk
    zipcode = models.CharField(max_length=6)  # PLZ
    state = models.CharField(max_length=48)  # Bundesland
    name = models.CharField(max_length=48)  # Gemeindenamen
    county = models.CharField(max_length=48)  # Kreisname

    def __unicode__(self):
        return self.name


class Recordsection(models.Model):
    ''' Meldestelle '''
    municipality = models.ForeignKey(Municipality)
    address = models.CharField(max_length=200)  # Anschrift
    city = models.CharField(max_length=48)  # Ort
    zipcode = models.CharField(max_length=6)  # PLZ
    street = models.CharField(max_length=48)  # Straße

    def __unicode__(self):
        return self.address


class Zipcode(models.Model):
    ''' Postleitzahl '''
    zipcode = models.CharField(max_length=6)  # PLZ
    state = models.CharField(max_length=48)  # Bundesland
    city = models.CharField(max_length=128)  # Ort
    key = models.CharField(max_length=10)

    def __unicode__(self):
        return self.zipcode


class Form(models.Model):
    ''' Uebermittlungssperre Formular '''
    state = models.CharField(max_length=48)  # Bundesland
    heading = models.CharField(max_length=200)
    religionclause = models.CharField(max_length=512, null=True, blank=True)
    partyclause = models.CharField(max_length=1024, null=True, blank=True)
    autoqueryclause = models.CharField(max_length=512, null=True, blank=True)
    jubileeclause = models.CharField(max_length=512, null=True, blank=True)
    directoryclause = models.CharField(max_length=512, null=True, blank=True)
    directmarketingclause = models.CharField(max_length=512, null=True, blank=True)
    militaryclause = models.CharField(max_length=512, null=True, blank=True)
    miscellaneousclause = models.CharField(max_length=512, null=True, blank=True)

    def __unicode__(self):
        return self.state
