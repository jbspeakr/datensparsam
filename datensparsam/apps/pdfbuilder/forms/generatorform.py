from django import forms
from datensparsam.apps.api import models as apimodels


class GeneratorForm(forms.Form):
    zipcode = forms.CharField(
        max_length=5,
        widget=forms.TextInput(attrs={'placeholder': '12051'}))
    registrationoffice = forms.CharField(
        required=False)
    municipality = forms.CharField(
        required=False)
    name = forms.CharField(
        max_length=32,
        widget=forms.TextInput(attrs={'placeholder': 'Mustermann'}))
    firstname = forms.CharField(
        max_length=32,
        widget=forms.TextInput(attrs={'placeholder': 'Maxi'}))
    address = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={'placeholder': 'Lindenstr. 6'}))
    city = forms.CharField(
        max_length=64,
        widget=forms.TextInput(attrs={'placeholder': 'Berlin'}))

    def clean(self):
        if self.has_registrationoffice() or self.has_municipality():
            return self.cleaned_data
        else:
            raise forms.ValidationError("No recipient found.")

    def has_registrationoffice(self):
        try:
            data = self.cleaned_data['registrationoffice']
            apimodels.RegistrationOffice.objects.get(id=data)
            return True
        except:
            return False

    def has_municipality(self):
        try:
            data = self.cleaned_data['municipality']
            apimodels.Municipality.objects.get(id=data)
            return True
        except apimodels.Municipality.DoesNotExist:
            return False
