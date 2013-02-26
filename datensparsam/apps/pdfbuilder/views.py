#!/usr/bin/python
# -*- coding: utf-8 -*-
# Fall back to StringIO in environments where cStringIO is not available
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

import datetime
from django.shortcuts import render
from django.http import HttpResponse

from datensparsam.apps.pdfbuilder import models
from datensparsam.apps.pdfbuilder.helpers import user as helper
from datensparsam.libs.pdf.reportlab_adaptor import SimplePdf
from datensparsam.apps.pdfbuilder.forms import requestform


def index(request):
    form = requestform.RequestForm()  # An unbound form
    return render(request, 'pdfbuilder/index.html', {
        'form': form,
    })


def get_pdf(request):
    if request.method == 'POST':
        form = requestform.RequestForm(request.POST)
        if form.is_valid():
            zipcode = request.POST['zipcode']
            stateID = request.POST['state']

            user = helper.User(
                request.POST['name'],
                request.POST['firstname'],
                request.POST['address'],
                request.POST['zipcode'],
                request.POST['city']
            )

            form = models.Form.objects.get(id=stateID)
            recordsection = query_recordsection(zipcode, form.state)
            return create_pdf_response(recordsection, user, form)
    else:
        form = requestform.RequestForm()  # An unbound form

    return render(request, 'pdfbuilder/index.html', {
        'form': form,
    })


def query_recordsection(zipcode, state):
    municipalityQuerySet = models.Municipality.objects.filter(
        zipcode=zipcode,
        state=state
    )

    if not municipalityQuerySet:
        recordsectionuerySet = models.Recordsection.objects.filter(
            city=state
        )

    else:
        recordsectionuerySet = models.Recordsection.objects.filter(
            municipality=municipalityQuerySet[0].key
        )

    if not recordsectionuerySet:
        # return error message
        return "No Recordsection available"
    else:
        return recordsectionuerySet[0]


def create_pdf_response(recordsection, user, form):
    ''' Returns PDF Response. '''
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="uebermittlungssperre.pdf"'

    # Create Buffer
    buff = StringIO()

    # Setup PDF
    doc = setup_pdf_content(buff, form, user, recordsection)
    doc.make()

    # Create Response and close Buffer
    response.write(buff.getvalue())
    buff.close()
    return response


def setup_pdf_content(buff, form, user, recordsection):
    ''' Adds content to a new PDF using SimplePdf class. '''
    now = datetime.datetime.now()

    address_sender = [
        user.name + ', ' + user.firstname,
        user.address,
        user.zip + ' ' + user.city
    ]

    address_recipient = [
        recordsection.address,
        recordsection.street,
        recordsection.zipcode + ' ' + recordsection.city
    ]

    doc = SimplePdf(buff)
    doc.add_address(address_sender)
    doc.add_address(address_recipient)
    doc.add_heading(form.heading)
    doc.add_paragraph('Hiermit widerspreche ich:', 0)

    doc.add_bulleted_paragraph(form.religionclause)
    doc.add_bulleted_paragraph(form.partyclause)
    doc.add_bulleted_paragraph(form.autoqueryclause)
    doc.add_bulleted_paragraph(form.jubileeclause)
    doc.add_bulleted_paragraph(form.directoryclause)
    doc.add_bulleted_paragraph(form.directmarketingclause)
    doc.add_bulleted_paragraph(form.militaryclause)
    doc.add_bulleted_paragraph(form.miscellaneousclause)

    doc.add_paragraph('Ich bitte um Bestätigung, dass der Widerspruch im Melderegister gespeichert worden ist.', 36)
    doc.add_paragraph('Unterschrift der/des Antragstellerin/-stellers', 48)
    doc.add_paragraph(user.city + ', den ' + now.strftime("%d.%m.%Y"), 0)

    return doc
