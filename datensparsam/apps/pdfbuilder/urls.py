from django.conf.urls import patterns, url

urlpatterns = patterns(
    'datensparsam.apps.pdfbuilder.views',
    url(r'^$', 'generator', {}, name='pdfbuilder-generator'),
    url(r'^pdf/$', 'pdf', {}, name='pdfbuilder-pdf'),
)
