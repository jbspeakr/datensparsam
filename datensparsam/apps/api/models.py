from django.db import models


class Municipality(models.Model):
    ''' Gemeinde '''
    key = models.CharField(max_length=8)  # Gemeindeschluessel
    kind = models.CharField(max_length=48)  # Gemeindetyp
    district = models.CharField(max_length=48)  # Regierungsbezirk
    state = models.CharField(max_length=48)  # Bundesland
    name = models.CharField(max_length=48)  # Gemeindenamen
    county = models.CharField(max_length=48)  # Kreisname

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('key',)


class RegistrationOffice(models.Model):
    ''' Einwohnermeldeamt '''
    name = models.CharField(max_length=200)  # Anschrift
    city = models.CharField(max_length=200)  # Ort
    code = models.CharField(max_length=5)  # PLZ
    street = models.CharField(max_length=200)
    lat = models.CharField(max_length=32)  # Breitengrad
    lng = models.CharField(max_length=32)  # Laengengrad

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('city',)


class Zipcode(models.Model):
    ''' Postleitzahl '''
    zipcode = models.CharField(max_length=5)
    municipalities = models.ManyToManyField(Municipality)
    registration_offices = models.ManyToManyField(RegistrationOffice)

    def __unicode__(self):
        return self.zipcode

    class Meta:
        ordering = ('zipcode',)
