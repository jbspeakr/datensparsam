from django.db import models


# class MunicipalityManager(models.Manager):
#     def get_by_natural_key(self, key):
#         return self.get(key=key)


class Municipality(models.Model):
    ''' Gemeinde '''
    key = models.CharField(max_length=16, primary_key=True)
    kind = models.CharField(max_length=48)
    district = models.CharField(max_length=48)
    zipcode = models.CharField(max_length=6)
    state = models.CharField(max_length=48)
    name = models.CharField(max_length=48)
    county = models.CharField(max_length=48)

    def __unicode__(self):
        return self.name


class Recordsection(models.Model):
    ''' Meldestelle '''
    municipality = models.ForeignKey(Municipality)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=48)
    zipcode = models.CharField(max_length=6)
    street = models.CharField(max_length=48)

    def __unicode__(self):
        return self.address
