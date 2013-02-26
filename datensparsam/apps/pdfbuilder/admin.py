from datensparsam.apps.pdfbuilder.models import Municipality
from datensparsam.apps.pdfbuilder.models import Recordsection
from datensparsam.apps.pdfbuilder.models import Form
from django.contrib import admin
from django import forms


class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ['name', 'zipcode']

admin.site.register(Municipality, MunicipalityAdmin)

admin.site.register(Recordsection)


class FormModelForm(forms.ModelForm):
    religionclause = forms.CharField(widget=forms.Textarea, required=False)
    partyclause = forms.CharField(widget=forms.Textarea, required=False)
    autoqueryclause = forms.CharField(widget=forms.Textarea, required=False)
    jubileeclause = forms.CharField(widget=forms.Textarea, required=False)
    directoryclause = forms.CharField(widget=forms.Textarea, required=False)
    directmarketingclause = forms.CharField(widget=forms.Textarea, required=False)
    militaryclause = forms.CharField(widget=forms.Textarea, required=False)
    miscellaneousclause = forms.CharField(widget=forms.Textarea, required=False)


class FormAdmin(admin.ModelAdmin):
    form = FormModelForm

admin.site.register(Form, FormAdmin)
