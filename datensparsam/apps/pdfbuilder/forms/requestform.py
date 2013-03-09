#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _

from datensparsam.apps.pdfbuilder.models import Form as State
from datensparsam.apps.pdfbuilder.models import Zipcode


class RequestForm(forms.Form):
    state = forms.ModelChoiceField(queryset=State.objects.all(), label='Dein Bundesland')
    name = forms.CharField(max_length=32, label='Dein Nachname', widget=forms.TextInput(attrs={'placeholder': 'Mustermann'}))
    firstname = forms.CharField(max_length=32, label='Dein Vorname', widget=forms.TextInput(attrs={'placeholder': 'Maxi'}))
    address = forms.CharField(max_length=200, label='Deine Anschrift', widget=forms.TextInput(attrs={'placeholder': 'Lindenstraße 6'}))
    zipcode = forms.CharField(max_length=5, min_length=5, label='Deine Postleitzahl', widget=forms.TextInput(attrs={'placeholder': '12345'}))
    city = forms.CharField(max_length=32, label='Deine Stadt', widget=forms.TextInput(attrs={'placeholder': 'Berlin'}))

    def clean(self):
        if self.cleaned_data.get("zipcode"):
            if not self.cleaned_data.get("zipcode").__len__() == 5:
                raise forms.ValidationError('Wrong zipcode length.')

        if not self.is_valid_zipcode(self.cleaned_data.get("zipcode"), self.cleaned_data.get("state")):
            raise forms.ValidationError(_('Zipcode not in state.'))
        return self.cleaned_data

    def is_valid_zipcode(self, zipcode, state):
        try:
            Zipcode.objects.get(zipcode=zipcode, state=state)
            return True
        except Zipcode.MultipleObjectsReturned:
            return True
        except Zipcode.DoesNotExist:
            return False
