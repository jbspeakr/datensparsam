# Fall back to StringIO in environments where cStringIO is not available
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse

from datensparsam.apps.pdfbuilder import models
from datensparsam.apps.pdfbuilder.helpers import user as helper
from datensparsam.apps.pdfbuilder.forms import requestform


def get_pdf(request):
    if request.method == 'POST':
        form = requestform.RequestForm(request.POST)
        if form.is_valid():
            municipalityZip = request.POST['municipalityZipcode']
            municipalityState = request.POST['municipalityState']

            user = helper.User(
                request.POST['userName'],
                request.POST['userFirstname'],
                request.POST['userAddress'],
                request.POST['userZipcode'],
                request.POST['userCity']
                )

            recordsection = query_recordsection(municipalityZip, municipalityState)
            return create_pdf_response(recordsection, user)


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


def create_pdf_response(recordsection, user):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="uebermittlungssperre.pdf"'

    buffer = StringIO()

    # Create the PDF object, using the StringIO object as its "file."
    form = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Setup Canvas Settings
    form.setFont('Helvetica', 12)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.

    # Create Recipient
    form.drawString(30, 705, recordsection.address)
    form.drawString(30, 690, recordsection.street)
    form.drawString(30, 675, recordsection.zipcode + ' ' + recordsection.city)

    # Create Sender
    form.drawString(500, 750, user.name + ', ' + user.firstname)
    form.drawString(500, 735, user.address)
    form.drawString(500, 720, user.zip + ' ' + user.city)

    # Close the PDF object cleanly.
    form.showPage()
    form.save()

    # Get the value of the StringIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
