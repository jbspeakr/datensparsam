#!/usr/bin/python
# -*- coding: utf-8 -*-
# Fall back to StringIO in environments where cStringIO is not available
from io import BytesIO

import datetime
# from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

from datensparsam.apps.pdfbuilder import models as pdfmodels
from datensparsam.apps.api import models as apimodels
# from datensparsam.apps.pdfbuilder.helpers import user
# from datensparsam.libs.pdf.reportlab_adaptor import SimplePdf
# from datensparsam.apps.pdfbuilder.forms import requestform

from dinbrief.document import Document
from dinbrief.template import BriefTemplate
from dinbrief.styles import styles
from reportlab.platypus import Paragraph
# from reportlab.platypus.flowables import Spacer


def pdf(request):
    ''' Returns PDF Response. '''
    if request.method == 'POST':
        date = datetime.datetime.now().strftime("%d.%m.%Y")

        sender_address = [
            request.POST['name'] + ', ' + request.POST['firstname'],
            request.POST['address'],
            request.POST['zipcode'] + ' ' + request.POST['city']
        ]

        if request.POST['registrationoffice']:
            pk = request.POST['registrationoffice']
            recipient = apimodels.RegistrationOffice.objects.get(
                pk=pk)
        elif request.POST['municipality']:
            pk = request.POST['municipality']
            recipient = apimodels.Municipality.objects.get(
                pk=pk)
        else:
            raise Exception('no receipient')

        recipient_address = [
            recipient.name,
            recipient.street,
            recipient.zipcode + ' ' + recipient.city,
        ]

        paragraphs = pdfmodels.Form.objects.get(state=recipient.state)

        content = []
        content.append(Paragraph(
            paragraphs.heading, styles['Subject']))
        content.append(Paragraph(
            _(u'Dear Sir or Madam'), styles['Greeting']))
        content.append(Paragraph(
            _(u'Contradiction intro'), styles['Greeting']))

        for paragraph in paragraphs.get_content():
            content.append(Paragraph('- ' + paragraph, styles['Message']))

        content.append(Paragraph(
            _(u'Request for Confirmation'), styles['Message']))
        content.append(Paragraph(
            _(u'Request for Forwarding'), styles['Normal']))
        content.append(Paragraph(_(u'Greetings'), styles['Closing']))
        content.append(Paragraph(
            '%s %s (%s)' % (request.POST['firstname'], request.POST['name'],
            _(u'Signature')), styles['Normal']))
        content.append(Paragraph(
            '%s, den %s' % (request.POST['city'], date), styles['Normal']))

        # Setup PDF
        document = Document(
            sender=sender_address,
            recipient=recipient_address,
            date=date,
            content=content
        )

        # Create Buffer
        buff = BytesIO()

        # Build template
        template = BriefTemplate(buff, document)
        template.build(document.content)

        # Create Response and close Buffer
        response = HttpResponse(mimetype='application/pdf')
        response['Content-Disposition'] = \
            'attachment; filename="uebermittlungssperre.pdf"'
        pdf = buff.getvalue()
        buff.close()

        response.write(pdf)
        return response


# def index(request):
#     if request.method == 'POST':
#         form = requestform.RequestForm(request.POST)
#         if form.is_valid():
#             zipcode = request.POST['zipcode']
#             stateID = request.POST['state']

#             user = helper.User(
#                 request.POST['name'],
#                 request.POST['firstname'],
#                 request.POST['address'],
#                 request.POST['zipcode'],
#                 request.POST['city']
#             )

#             form_entry = models.Form.objects.get(id=stateID)
#             recordsection = query_record_section(zipcode, form_entry.state)
#             response = create_pdf_response(recordsection, user, form_entry)
#             return response
#     else:
#         form = requestform.RequestForm()  # An unbound form

#     return render(request, 'pdfbuilder/index.html', {
#         'form': form,
#     })


# def query_record_section(zipcode, state):
#     try:
#         # Get corresponding municipality key
#         municipality_key = models.Municipality.objects.get(
#             zipcode=zipcode,
#             state=state
#         ).key
#     except models.Municipality.DoesNotExist:
#         # Get all zipcodes for corresponding city
#         zip_key = models.Zipcode.objects.filter(zipcode=zipcode, state=state)[0].key
#         zipcodes = models.Zipcode.objects.filter(key=zip_key, state=state)
#         municipality_key = ''

#         for code in zipcodes:
#             # Check if zipcode matches municipality zipcode
#             municipality_entry = models.Municipality.objects.filter(
#                 zipcode=code.zipcode,
#                 state=state
#             )
#             if municipality_entry.__len__() > 0:
#                 municipality_key = municipality_entry[0].key
#                 break

#         if not municipality_key:
#             municipality_key = models.Municipality.objects.filter(
#                 pk__startswith=zip_key
#             )[0].key

#     except models.Municipality.MultipleObjectsReturned:
#         # If there are multiple municipalities, choose first one
#         municipality_key = models.Municipality.objects.filter(
#             zipcode=zipcode,
#             state=state
#         )[0].key

#     # If there is a municipality, get corresponding record section
#     return models.Recordsection.objects.get(
#         municipality=municipality_key
#     )


# def create_pdf_response(recordsection, user, form):
#     ''' Returns PDF Response. '''
#     # Create the HttpResponse object with the appropriate PDF headers.
#     response = HttpResponse(mimetype='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="uebermittlungssperre.pdf"'

#     # Create Buffer
#     buff = StringIO()

#     # Setup PDF
#     doc = setup_pdf_content(buff, form, user, recordsection)
#     doc.make()

#     # Create Response and close Buffer
#     response.write(buff.getvalue())
#     buff.close()
#     return response


# def setup_pdf_content(buff, form, user, recordsection):
#     ''' Adds content to a new PDF using SimplePdf class. '''
#     now = datetime.datetime.now()

#     address_sender = [
#         user.name + ', ' + user.firstname,
#         user.address,
#         user.zip + ' ' + user.city
#     ]

#     address_recipient = [
#         recordsection.address,
#         recordsection.street,
#         recordsection.zipcode + ' ' + recordsection.city
#     ]

#     doc = SimplePdf(buff)
#     doc.add_address(address_sender)
#     doc.add_address(address_recipient)
#     doc.add_heading(form.heading)
#     doc.add_paragraph(_(u'Contradiction intro'), 0)

#     doc.add_bulleted_paragraph(form.religionclause)
#     doc.add_bulleted_paragraph(form.partyclause)
#     doc.add_bulleted_paragraph(form.autoqueryclause)
#     doc.add_bulleted_paragraph(form.jubileeclause)
#     doc.add_bulleted_paragraph(form.directoryclause)
#     doc.add_bulleted_paragraph(form.directmarketingclause)
#     doc.add_bulleted_paragraph(form.militaryclause)
#     doc.add_bulleted_paragraph(form.miscellaneousclause)

#     doc.add_paragraph(_(u'Request for Confirmation'), 36)
#     doc.add_paragraph(_(u'Request for Forwarding'), 0)
#     doc.add_paragraph(('%s %s (%s)') % (user.firstname, user.name, _(u'Signature')), 48)
#     doc.add_paragraph(('%s, %s') % (user.city, now.strftime("%d.%m.%Y")), 0)

#     return doc
