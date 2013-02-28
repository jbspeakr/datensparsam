#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from datensparsam.apps.pdfbuilder.models import Form as State
from datensparsam.apps.pdfbuilder.models import Zipcode


class RequestForm(forms.Form):
    state = forms.ModelChoiceField(queryset=State.objects.all(), label='Dein Bundesland')
    name = forms.CharField(max_length=32, label='Dein Vorname')
    firstname = forms.CharField(max_length=32, label='Dein Nachname')
    address = forms.CharField(max_length=200, label='Deine Anschrift')
    zipcode = forms.IntegerField(label='Deine Postleitzahl')
    city = forms.CharField(max_length=32, label='Deine Stadt')

    def clean(self):
        if not self.is_valid_zipcode(self.cleaned_data.get("zipcode"), self.cleaned_data.get("state")):
            raise forms.ValidationError("Invalid zipcode.")
        return self.cleaned_data

    def is_valid_zipcode(self, zipcode, state):
        try:
            Zipcode.objects.get(zipcode=zipcode, state=state)
            return True
        except Zipcode.MultipleObjectsReturned:
            return True
        except Zipcode.DoesNotExist:
            return False
