from django.conf.urls import patterns, url


urlpatterns = patterns(
    'datensparsam.apps.pdfbuilder.views',
    url(r'^$', 'index', {}, name='index'),
)
