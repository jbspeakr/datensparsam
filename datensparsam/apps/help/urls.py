from django.conf.urls import patterns, url


urlpatterns = patterns(
    'datensparsam.apps.help.views',
    # Examples:
    # url(r'^$', 'datensparsam.views.home', name='home'),
    # url(r'^datensparsam/', include('datensparsam.foo.urls')),
    #url(r'^$', 'index', {}, name='index'),
    url(r'^ueber-uns/', 'about', {}, name='help-about'),
    url(r'^datenschutz/', 'privacy', {}, name='help-privacy'),
    url(r'^faq/', 'faq', {}, name='help-faq'),
)
