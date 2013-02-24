#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from datensparsam.apps.pdfbuilder.models import Form as State


class RequestForm(forms.Form):
    state = forms.ModelChoiceField(queryset=State.objects.all())
    name = forms.CharField(max_length=32)
    firstname = forms.CharField(max_length=32)
    address = forms.CharField(max_length=200)
    zipcode = forms.CharField(max_length=6)
    city = forms.CharField(max_length=32)
