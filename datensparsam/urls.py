from django.conf.urls import patterns, include, url

# from datensparsam.apps.pdfbuilder import views as pdfbuilder

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'datensparsam.views.home', name='home'),
    # url(r'^datensparsam/', include('datensparsam.foo.urls')),
    # url(r'^$', 'index', {}, name='home'),
    url(r'^$', include('datensparsam.apps.pdfbuilder.urls')),
    #url(r'^form/', include('datensparsam.apps.pdfbuilder.urls')),
    url(r'^hilfe/', include('datensparsam.apps.pdfbuilder.sub_urls')),
    # url(r'^pdfbuilder/', pdfbuilder.get_pdf, {}, name='pdfbuilder'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^api/', include('datensparsam.apps.api.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
