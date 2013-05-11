from django.conf.urls import patterns, url

urlpatterns = patterns(
    'datensparsam.apps.pdfbuilder.views',
    url(r'^$', 'generator', {}, name='pdfbuilder-generator'),
    url(r'^download/$', 'download', {}, name='pdfbuilder-download'),
    url(r'^download/pdf/$', 'pdf', {}, name='pdfbuilder-pdf'),
)
