from datensparsam.apps.api import models
from tastypie.resources import ModelResource
from tastypie import fields


class MunicipalityResource(ModelResource):
    class Meta:
        queryset = models.Municipality.objects.all()
        resource_name = 'municipality'
        filtering = {
            "zipcode": ('exact', 'startswith',),
        }
        include_resource_uri = False


class RegistrationOfficeResource(ModelResource):
    class Meta:
        queryset = models.RegistrationOffice.objects.all()
        resource_name = 'registration_office'
        filtering = {
            "zipcode": ('exact', 'startswith',),
        }
        include_resource_uri = False


class ZipcodeResource(ModelResource):
    municipalities = fields.ToManyField(
        'datensparsam.apps.api.api.MunicipalityResource',
        'municipalities',
        related_name='zipcodes',
        full=True)

    registration_offices = fields.ToManyField(
        'datensparsam.apps.api.api.RegistrationOfficeResource',
        'registrationoffices',
        related_name='zipcodes',
        null=True, blank=True,
        full=True)

    class Meta:
        queryset = models.Zipcode.objects.all()
        resource_name = 'zipcode'
        filtering = {
            "zipcode": ('exact', 'startswith',),
        }
        include_resource_uri = False
