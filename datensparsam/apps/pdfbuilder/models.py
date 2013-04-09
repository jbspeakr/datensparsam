#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models


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
