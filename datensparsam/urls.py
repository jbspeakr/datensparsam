from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', include('datensparsam.apps.pdfbuilder.urls')),
    url(r'^hilfe/', include('datensparsam.sub_urls')),
    url(r'^api/', include('datensparsam.apps.api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
