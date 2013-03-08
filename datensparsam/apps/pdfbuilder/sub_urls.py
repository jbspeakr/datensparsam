from django.conf.urls import patterns
from django.views.generic import TemplateView


def TV(template):
    return TemplateView.as_view(template_name=template)

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'datensparsam.views.home', name='home'),
    # url(r'^datensparsam/', include('datensparsam.foo.urls')),
    #url(r'^$', 'index', {}, name='index'),
    (r'^ueber-uns/', TV('help/about.html'), {}, 'help-about'),
    (r'^datenschutz/', TV('help/privacy.html'), {}, 'help-privacy'),
    (r'^faq/', TV('help/faq.html'), {}, 'help-faq'),
)
