from django.db import models


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
    id = models.AutoField(primary_key=True)
    key = models.ForeignKey(Municipality)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=48)
    zipcode = models.CharField(max_length=6)
    street = models.CharField(max_length=48)

    def __unicode__(self):
        return self.address
