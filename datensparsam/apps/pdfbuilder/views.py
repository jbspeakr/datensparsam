from io import BytesIO

import datetime
import logging
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from django.views.decorators.http import require_POST

from datensparsam.apps.pdfbuilder import models as pdfmodels
from datensparsam.apps.api import models as apimodels

from dinbrief.document import Document
from dinbrief.template import BriefTemplate
from dinbrief.styles import styles
from reportlab.platypus import Paragraph


# Get an instance of a logger
logger = logging.getLogger(__name__)


@require_POST
def pdf(request):
    ''' Returns PDF Response. '''
    sender_address = create_sender_address(request)
    recipient = get_recipient(request)
    recipient_address = create_recipient_address(recipient)
    content = create_content(request, recipient)

    date = datetime.datetime.now().strftime("%d.%m.%Y")

    # Setup PDF
    document = Document(
        sender=sender_address,
        recipient=recipient_address,
        date=date,
        content=content
    )

    response = create_pdf_response(document)
    return response


def generator(request):
    context = {}
    if request.method == 'POST':
        zipcode = request.POST['zipcode']

        context = {
            "zipcode": zipcode,

        }
    return render(request, "generator.html", context)


def get_recipient(request):
    recipient = ""
    if request.POST['registrationoffice']:
        pk = request.POST['registrationoffice']
        recipient = apimodels.RegistrationOffice.objects.get(pk=pk)
    elif request.POST['municipality']:
        pk = request.POST['municipality']
        recipient = apimodels.Municipality.objects.get(pk=pk)
    else:
        # TODO return proper Error Page
        raise Exception('no receipient')

    return recipient


def create_content(request, recipient):
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

    return content


def create_recipient_address(recipient):
    recipient_address = [
        recipient.name,
        recipient.street,
        recipient.zipcode + ' ' + recipient.city,
    ]
    return recipient_address


def create_sender_address(request):
    sender_address = [
        request.POST['name'] + ', ' + request.POST['firstname'],
        request.POST['address'],
        request.POST['zipcode'] + ' ' + request.POST['city']
    ]
    return sender_address


def create_pdf_response(document):
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
