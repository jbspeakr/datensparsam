
from datensparsam.apps.pdfbuilder.models import Municipality
from datensparsam.apps.pdfbuilder.models import Recordsection


#def build_pdf(request):
    # if request.method == 'POST':
    #     municipalityZip = request.POST['municipalityZip']
    #     municipalityName = request.POST['municipalityName']
    #     userName = request.POST['userName']
    #     userFirstname = request.POST['userFirstname']
    #     userAddress = request.POST['userAddress']
    #     userZip = request.POST['userZip']
    #     userCity = request.POST['userCity']

    #     recordsection = query_recordsection(municipalityZip, municipalityName)


# def query_recordsection(municipalityZip, municipalityName):
#     municipality = Municipality.objects.filter(zipcode=municipalityZip, name=municipalityName)
#     if not municipality:
#         # return error message
#         return ""
#     else:
#         recordsection = Recordsection.objects.filter(municipality=municipality.key)
#         return recordsection
