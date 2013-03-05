from django.conf.urls import patterns, url


urlpatterns = patterns(
    'datensparsam.apps.pdfbuilder.views',
    # Examples:
    # url(r'^$', 'datensparsam.views.home', name='home'),
    # url(r'^datensparsam/', include('datensparsam.foo.urls')),
    url(r'^$', 'index', {}, name='index'),
)
