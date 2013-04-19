from django.conf.urls import patterns, include
from tastypie.api import Api
from datensparsam.apps.api import api

v1_api = Api(api_name='v1')
v1_api.register(api.RegistrationOfficeResource())
v1_api.register(api.MunicipalityResource())
v1_api.register(api.ZipcodeResource())

urlpatterns = patterns(
    '',
    (r'^', include(v1_api.urls)),
)
