#!/usr/bin/python
# -*- coding: utf-8 -*-
# Fall back to StringIO in environments where cStringIO is not available
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

import datetime
# from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

# from datensparsam.apps.pdfbuilder import models
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
        sender = [
            request.POST['name'] + request.POST['firstname'],
            request.POST['address'],
            request.POST['zipcode'] + request.POST['city']
        ]

        recipient = [

        ]

        paragraphs = models.Form.objects.get(id=stateID)
        content = [
            Paragraph(paragraphs.heading, styles['Subject']),
            Paragraph(_(u'Contradiction intro'), styles['Greeting']),
            Paragraph(paragraphs.partyclause, styles['Normal']),
            Paragraph(paragraphs.autoqueryclause, styles['Normal']),
            Paragraph(paragraphs.jubileeclause, styles['Normal']),
            Paragraph(paragraphs.directoryclause, styles['Normal']),
            Paragraph(paragraphs.directmarketingclause, styles['Normal']),
            Paragraph(paragraphs.religionclause, styles['Normal']),
            Paragraph(paragraphs.militaryclause, styles['Normal']),
            Paragraph(paragraphs.miscellaneousclause, styles['Normal']),
            Paragraph(_(u'Request for Confirmation'), styles['Normal']),
            Paragraph(_(u'Request for Forwarding'), styles['Normal']),
            Paragraph('%s %s (%s)' %
                      request.POST['firstname'],
                      request.POST['name'],
                      _(u'Signature'),
                      styles['Closing']),
            Paragraph('%s, %s' %
                      request.POST['city'],
                      date,
                      styles['Signature']),
        ]

        #     doc.add_paragraph(_(u'Request for Confirmation'), 36)
#     doc.add_paragraph(_(u'Request for Forwarding'), 0)
#     doc.add_paragraph(('%s %s (%s)') % (user.firstname, user.name, _(u'Signature')), 48)
#     doc.add_paragraph(('%s, %s') % (user.city, now.strftime("%d.%m.%Y")), 0)

        # Create Buffer
        buff = StringIO()

        # Setup PDF
        document = Document(
            sender=sender,
            recipient=recipient,
            date=date,
            content=content
        )
        template = BriefTemplate(buff, document)
        template.build(document.content)

        # Create Response and close Buffer
        response = HttpResponse(mimetype='application/pdf')
        response['Content-Disposition'] = \
            'attachment; filename="uebermittlungssperre.pdf"'
        response.write(template)
        buff.close()
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
