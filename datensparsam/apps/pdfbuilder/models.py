from unittest import TestCase
from django.db import models


class Form(models.Model):
    """ Uebermittlungssperre Formular """
    state = models.CharField(max_length=48)
    heading = models.CharField(max_length=200)
    religion_clause = models.CharField(max_length=512, null=True, blank=True)
    party_clause = models.CharField(max_length=1024, null=True, blank=True)
    auto_query_clause = models.CharField(max_length=512, null=True, blank=True)
    jubilee_clause = models.CharField(max_length=512, null=True, blank=True)
    directory_clause = models.CharField(max_length=512, null=True, blank=True)
    direct_marketing_clause = models.CharField(max_length=512, null=True, blank=True)
    military_clause = models.CharField(max_length=512, null=True, blank=True)
    miscellaneous_clause = models.CharField(max_length=512, null=True, blank=True)

    def __unicode__(self):
        return self.state

    def get_content(self):
        content = []
        if self.religion_clause:
            content.append(self.religion_clause)
        if self.party_clause:
            content.append(self.party_clause)
        if self.auto_query_clause:
            content.append(self.auto_query_clause)
        if self.jubilee_clause:
            content.append(self.jubilee_clause)
        if self.directory_clause:
            content.append(self.directory_clause)
        if self.direct_marketing_clause:
            content.append(self.direct_marketing_clause)
        if self.military_clause:
            content.append(self.military_clause)
        if self.miscellaneous_clause:
            content.append(self.miscellaneous_clause)
        return content
