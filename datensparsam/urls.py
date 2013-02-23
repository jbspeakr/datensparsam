from django.conf.urls import patterns, include, url

from datensparsam.apps.pdfbuilder.views import Recordsection

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('datensparsam.urls',
    # Examples:
    # url(r'^$', 'datensparsam.views.home', name='home'),
    # url(r'^datensparsam/', include('datensparsam.foo.urls')),
    # url(r'^pdfbuilder/', views.hack, {}, name='domainhack'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
