from django import forms


class RequestForm(forms.Form):
    municipalityZipcode = forms.CharField(max_length=6)
    municipalityState = forms.CharField(max_length=48)
    userName = forms.CharField(max_length=32)
    userFirstname = forms.CharField(max_length=32)
    userAddress = forms.CharField(max_length=200)
    userZipcode = forms.CharField(max_length=6)
    userCity = forms.CharField(max_length=32)
