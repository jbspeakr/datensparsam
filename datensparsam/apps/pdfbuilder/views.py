#!/usr/bin/python
# -*- coding: utf-8 -*-
# Fall back to StringIO in environments where cStringIO is not available
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from django.http import HttpResponse

from datensparsam.apps.pdfbuilder import models
from datensparsam.apps.pdfbuilder.helpers import user as helper
from datensparsam.apps.pdfbuilder.helpers import pdf
from datensparsam.apps.pdfbuilder.forms import requestform


def get_pdf(request):
    if request.method == 'POST':
        form = requestform.RequestForm(request.POST)
        if form.is_valid():
            municipalityZip = request.POST['zipcode']
            municipalityState = request.POST['state']

            user = helper.User(
                request.POST['name'],
                request.POST['firstname'],
                request.POST['address'],
                request.POST['zipcode'],
                request.POST['city']
                )

            FormQuerySet = models.Form.objects.filter(id=municipalityState)
            recordsection = query_recordsection(municipalityZip, FormQuerySet[0].state)
            return create_pdf_response(recordsection, user, FormQuerySet[0])


def query_recordsection(municipalityZip, municipalityState):
    municipalityQuerySet = models.Municipality.objects.filter(
        zipcode=municipalityZip,
        state=municipalityState
        )
    if not municipalityQuerySet:
        # return error message
        return "No Municipality available"
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
    address_sender = [user.name + ', ' + user.firstname, user.address, user.zip + ' ' + user.city]
    address_recipient = [recordsection.address, recordsection.street, recordsection.zipcode + ' ' + recordsection.city]

    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="uebermittlungssperre.pdf"'

    buff = StringIO()

    doc = pdf.Pdf(buff)

    doc.add_address(address_sender)
    doc.add_address(address_recipient)
    doc.add_heading(form.heading)
    doc.add_paragraph('Hiermit widerspreche ich:')

    doc.add_paragraph(form.religionclause)
    doc.add_paragraph(form.partyclause)
    doc.add_paragraph(form.autoqueryclause)
    doc.add_paragraph(form.jubileeclause)
    doc.add_paragraph(form.directoryclause)
    doc.add_paragraph(form.directmarketingclause)
    doc.add_paragraph(form.militaryclause)
    doc.add_paragraph(form.miscellaneousclause)

    doc.add_paragraph('Ich bitte um Bestätigung, dass der Widerspruch im Melderegister gespeichert worden ist.')
    doc.add_paragraph('(Unterschrift der/des Antragstellerin/-stellers)')

    doc.make()
    response.write(buff.getvalue())
    buff.close()
    return response

    # doc = SimpleDocTemplate(buff, pagesize=letter,
    #                     rightMargin=72, leftMargin=72,
    #                     topMargin=72, bottomMargin=18)

    # Story = []

    # styles = getSampleStyleSheet()
    # styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

    # address_recipient = [recordsection.address, recordsection.street, recordsection.zipcode + ' ' + recordsection.city]
    # address_sender = [user.name + ', ' + user.firstname, user.address, user.zip + ' ' + user.city]

    # for part in address_sender:
    #     ptext = '<font size=12>%s</font>' % part.strip()
    #     Story.append(Paragraph(ptext, styles["Normal"]))

    # Story.append(Spacer(1, 12))

    # for part in address_recipient:
    #     ptext = '<font size=12>%s</font>' % part.strip()
    #     Story.append(Paragraph(ptext, styles["Normal"]))

    # Story.append(Spacer(1, 12))

    # ptext = form.heading
    # Story.append(Paragraph(ptext, styles["Normal"]))

    # Story.append(Spacer(1, 12))

    # ptext = 'Hiermit widerspreche ich'
    # Story.append(Paragraph(ptext, styles["Normal"]))

    # ptext = form.religionclause
    # Story.append(Paragraph(ptext, styles["Normal"]))

    # doc.build(Story)
    # response.write(buff.getvalue())
    # buff.close()
    # return response
