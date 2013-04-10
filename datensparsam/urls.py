from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()


def TV(template):
    return TemplateView.as_view(template_name=template)

urlpatterns = patterns(
    '',
    (r'^$', TV('index.html'), {}, 'index'),
    (r'^generator/', TV('generator.html'), {}, 'generator'),
    (r'^informationen/', TV('information.html'), {}, 'informationen'),
    (r'^ueber-uns/', TV('about.html'), {}, 'about'),
    (r'^impressum/', TV('imprint.html'), {}, 'imprint'),
    (r'^nutzungsbedingungen/', TV('tos.html'), {}, 'tos'),
    (r'^datenschutz/', TV('privacy.html'), {}, 'privacy'),

    url(r'^pdf/', include('datensparsam.apps.pdfbuilder.urls')),
    url(r'^api/', include('datensparsam.apps.api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
