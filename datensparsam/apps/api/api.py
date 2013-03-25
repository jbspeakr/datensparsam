from datensparsam.apps.api import models
from tastypie.resources import ModelResource


class MunicipalityResource(ModelResource):
    class Meta:
        queryset = models.Municipality.objects.all()
        resource_name = 'municipality'
        filtering = {
            "zipcode": ('exact', 'startswith',),
        }


class RegistrationOfficeResource(ModelResource):
    class Meta:
        queryset = models.RegistrationOffice.objects.all()
        resource_name = 'registration_office'
        filtering = {
            "zipcode": ('exact', 'startswith',),
        }
