from django import forms
from django.utils.translation import ugettext_lazy as _

from datensparsam.apps.api import models as apimodels


class GeneratorForm(forms.Form):
    zipcode = forms.CharField(
        max_length=5,
        widget=forms.TextInput(
            attrs={
                'placeholder': '12051',
                'required': 'true'
            }))
    registrationoffice = forms.CharField(
        required=False)
    municipality = forms.CharField(
        required=False)
    name = forms.CharField(
        max_length=32,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Mustermann',
                'required': 'true'
            }))
    firstname = forms.CharField(
        max_length=32,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Maxi',
                'required': 'true'
            }))
    address = forms.CharField(
        max_length=64,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Lindenstr. 6',
                'required': 'true'
            }))
    city = forms.CharField(
        max_length=64,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Berlin',
                'required': 'true'
            }))

    def clean(self):
        if self.has_registrationoffice() or self.has_municipality():
            return self.cleaned_data
        else:
            raise forms.ValidationError(_("No recipient found."))

    def has_registrationoffice(self):
        try:
            data = self.cleaned_data['registrationoffice']
            if data == '':
                return False
            apimodels.RegistrationOffice.objects.get(id=data)
            return True
        except:
            return False

    def has_municipality(self):
        try:
            data = self.cleaned_data['municipality']
            if data == '':
                return False
            apimodels.Municipality.objects.get(id=data)
            return True
        except apimodels.Municipality.DoesNotExist:
            return False
