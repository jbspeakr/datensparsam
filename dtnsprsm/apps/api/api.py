from tastypie.resources import ModelResource
from tastypie import fields

from dtnsprsm.apps.api import models


class MunicipalityResource(ModelResource):
    class Meta(object):
        queryset = models.Municipality.objects.all()
        resource_name = 'municipality'
        filtering = {
            "zipcode": ('exact', 'startswith',),
        }
        include_resource_uri = False


class RegistrationOfficeResource(ModelResource):
    class Meta(object):
        queryset = models.RegistrationOffice.objects.all()
        resource_name = 'registration-office'


class ZipcodeResource(ModelResource):
    municipalities = fields.ToManyField(
        'dtnsprsm.apps.api.api.MunicipalityResource',
        'municipalities',
        related_name='zipcodes',
        full=True)

    registrationoffices = fields.ToManyField(
        'dtnsprsm.apps.api.api.RegistrationOfficeResource',
        'registrationoffices',
        related_name='zipcodes',
        null=True, blank=True,
        full=True)

    class Meta(object):
        queryset = models.Zipcode.objects.all()
        resource_name = 'zipcode'
        filtering = {
            "zipcode": ('exact', 'startswith',),
        }
        include_resource_uri = False
