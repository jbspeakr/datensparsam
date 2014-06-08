from io import BytesIO

import datetime
import logging

from django.http import HttpResponse, HttpResponseRedirect
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render
from django.core.urlresolvers import reverse

from datensparsam.apps.pdfbuilder import models as pdfmodels
from datensparsam.apps.pdfbuilder.forms import generatorform as forms
from datensparsam.apps.api import models as apimodels

from dinbrief.document import Document
from dinbrief.template import BriefTemplate
from dinbrief.styles import styles
from reportlab.platypus import Paragraph

# Get an instance of a logger
logger = logging.getLogger(__name__)


def download(request):
    return render(request, 'download.html')


def pdf(request):
    """ Returns PDF Response. """
    form = forms.GeneratorForm(request.session.get('form_data'))
    if form.is_valid():
        sender_address = create_sender_address(form)
        recipient = get_recipient(form)
        recipient_address = create_recipient_address(recipient)
        content = create_content(form, recipient)

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
    else:
        return HttpResponseRedirect(reverse('pdfbuilder-generator'))


def generator(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = forms.GeneratorForm(request.POST)  # A form bound to POST data
        if form.is_valid():  # All validation rules pass
            request.session['form_data'] = form.cleaned_data
            return HttpResponseRedirect(reverse('pdfbuilder-download'))
    else:
        form = forms.GeneratorForm()  # An unbound form

    return render(request, 'generator.html', {
        'form': form,
    })


def get_recipient(form):
    if form.cleaned_data['registrationoffice']:
        pk = form.cleaned_data['registrationoffice']
        recipient = apimodels.RegistrationOffice.objects.get(pk=pk)
    elif form.cleaned_data['municipality']:
        pk = form.cleaned_data['municipality']
        recipient = apimodels.Municipality.objects.get(pk=pk)
    else:
        # TODO return proper Error Page
        raise Exception('no recipient')

    return recipient


def create_content(form, recipient):
    paragraphs = pdfmodels.Form.objects.get(state=recipient.state)

    content = [Paragraph(
        paragraphs.heading, styles['Subject']), Paragraph(
        _(u'Dear Sir or Madam'), styles['Greeting']), Paragraph(
        _(u'Contradiction intro'), styles['Greeting'])]

    for paragraph in paragraphs.get_content():
        content.append(Paragraph('- ' + paragraph, styles['Message']))

    content.append(Paragraph(
        _(u'Request for Confirmation'), styles['Message']))
    content.append(Paragraph(
        _(u'Request for Forwarding'), styles['Normal']))
    content.append(Paragraph(_(u'Greetings'), styles['Closing']))
    content.append(Paragraph(
        '%s %s (%s)' % (form.cleaned_data['firstname'], form.cleaned_data['name'],
                        _(u'Signature')), styles['Normal']))

    return content


def create_recipient_address(recipient):
    recipient_address = [
        recipient.name,
        recipient.street,
        recipient.zipcode + ' ' + recipient.city,
    ]
    return recipient_address


def create_sender_address(form):
    sender_address = [
        form.cleaned_data['name'] + ', ' + form.cleaned_data['firstname'],
        form.cleaned_data['address'],
        form.cleaned_data['zipcode'] + ' ' + form.cleaned_data['city']
    ]
    return sender_address


def create_pdf_response(document):
    # Create Buffer
    buff = BytesIO()

    # Build template
    template = BriefTemplate(buff, document)
    template.build(document.content)

    # Create Response and close Buffer
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = \
        'attachment; filename="uebermittlungssperre.pdf"'

    pdf_response = buff.getvalue()
    buff.close()
    response.write(pdf_response)

    return response
