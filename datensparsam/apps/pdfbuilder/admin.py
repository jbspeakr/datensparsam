from datensparsam.apps.pdfbuilder.models import Municipality
from datensparsam.apps.pdfbuilder.models import Recordsection
from datensparsam.apps.pdfbuilder.models import Form
from django.contrib import admin


class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ['name', 'zipcode']

admin.site.register(Municipality, MunicipalityAdmin)

admin.site.register(Recordsection)

admin.site.register(Form)
