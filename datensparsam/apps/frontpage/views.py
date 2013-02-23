from django.shortcuts import render

from datensparsam.apps.pdfbuilder.forms import requestform


def index(request):
    form = requestform.RequestForm()  # An unbound form
    return render(
        request,
        'frontpage/index.html',
        {'form': form, }
        )
