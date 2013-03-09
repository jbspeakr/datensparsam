#!/usr/bin/python
# -*- coding: utf-8 -*-
# Fall back to StringIO in environments where cStringIO is not available
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

import datetime
from django.shortcuts import render
from django.http import HttpResponse, Http404

from datensparsam.apps.pdfbuilder import models
from datensparsam.apps.pdfbuilder.helpers import user as helper
from datensparsam.libs.pdf.reportlab_adaptor import SimplePdf
from datensparsam.apps.pdfbuilder.forms import requestform


def index(request):
    if request.method == 'POST':
        form = requestform.RequestForm(request.POST)
        if form.is_valid():
            zipcode = request.POST['zipcode']
            stateID = request.POST['state']
            city = request.POST['city']

            user = helper.User(
                request.POST['name'],
                request.POST['firstname'],
                request.POST['address'],
                request.POST['zipcode'],
                request.POST['city']
            )

            form = models.Form.objects.get(id=stateID)
            recordsection = query_recordsection(zipcode, city, form.state)
            return create_pdf_response(recordsection, user, form)
    else:
        form = requestform.RequestForm()  # An unbound form

    return render(request, 'pdfbuilder/index.html', {
        'form': form,
    })


def query_recordsection(zipcode, city, state):
    try:
        # Get corresponding municipality
        municipality_entry = models.Municipality.objects.get(
            zipcode=zipcode,
            state=state
        )
        # If there is a municipality, get corresponding record section
        record_section_entry = models.Recordsection.objects.get(
            municipality=municipality_entry.key
        )
    except models.Municipality.DoesNotExist:
        try:
            # If there is no corresponding municipality,
            # there seems to be one record section for a bunch of zipcodes,
            # like for Berlin: city == state
            record_section_entry = models.Recordsection.objects.get(
                city=state
            )
        except models.Recordsection.DoesNotExist:
            record_section_entry = models.Recordsection.objects.filter(
                city=city
            )[0]
        except models.Recordsection.MultipleObjectsReturned:
            # If there are more than just one record section,
            # choose the first one you can get
            record_section_entry = models.Recordsection.objects.filter(
                city=state
            )[0]
    except models.Recordsection.DoesNotExist:
        # No corresponding record section could be found at all
        raise Http404

    return record_section_entry


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
    doc.add_paragraph('Mit Bezug auf das Recht auf informationelle Selbstbestimmung widerspreche ich hiermit:', 0)

    doc.add_bulleted_paragraph(form.religionclause)
    doc.add_bulleted_paragraph(form.partyclause)
    doc.add_bulleted_paragraph(form.autoqueryclause)
    doc.add_bulleted_paragraph(form.jubileeclause)
    doc.add_bulleted_paragraph(form.directoryclause)
    doc.add_bulleted_paragraph(form.directmarketingclause)
    doc.add_bulleted_paragraph(form.militaryclause)
    doc.add_bulleted_paragraph(form.miscellaneousclause)

    doc.add_paragraph('Ich bitte um Bestätigung, dass der Widerspruch im Melderegister gespeichert worden ist.', 36)
    doc.add_paragraph(user.firstname + ' ' + user.name + ' (Unterschrift)', 48)
    doc.add_paragraph(user.city + ', den ' + now.strftime("%d.%m.%Y"), 0)

    return doc
