from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()


def TV(template):
    return TemplateView.as_view(template_name=template)

urlpatterns = patterns(
    '',
    url(r'^$', TV('index.html'), {}, 'index'),
    url(r'^informationen/$', TV('information.html'), {}, name='information'),
    url(r'^ueber-uns/$', TV('about.html'), {}, name='about'),
    url(r'^impressum/$', TV('imprint.html'), {}, name='imprint'),
    url(r'^nutzungsbedingungen/$', TV('tos.html'), {}, name='tos'),
    url(r'^datenschutz/$', TV('privacy.html'), {}, name='privacy'),

    url(r'^generator/', include('datensparsam.apps.pdfbuilder.urls')),

    url(r'^api/', include('datensparsam.apps.api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
