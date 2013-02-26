from datensparsam.apps.pdfbuilder.models import Municipality, Recordsection, Form, Zipcode
from django.contrib import admin
from django import forms


class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ['name', 'zipcode']


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


admin.site.register(Municipality, MunicipalityAdmin)
admin.site.register(Form, FormAdmin)
admin.site.register(Recordsection)
admin.site.register(Zipcode)
