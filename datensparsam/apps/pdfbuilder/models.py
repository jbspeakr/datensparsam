from django.db import models


class Form(models.Model):
    ''' Uebermittlungssperre Formular '''
    state = models.CharField(max_length=48)  # Bundesland
    heading = models.CharField(max_length=200)
    religionclause = models.CharField(max_length=512, null=True, blank=True)
    partyclause = models.CharField(max_length=1024, null=True, blank=True)
    autoqueryclause = models.CharField(max_length=512, null=True, blank=True)
    jubileeclause = models.CharField(max_length=512, null=True, blank=True)
    directoryclause = models.CharField(max_length=512, null=True, blank=True)
    directmarketingclause = models.CharField(max_length=512, null=True, blank=True)
    militaryclause = models.CharField(max_length=512, null=True, blank=True)
    miscellaneousclause = models.CharField(max_length=512, null=True, blank=True)

    def __unicode__(self):
        return self.state

    def get_content(self):
        content = []
        if self.religionclause:
            content.append(self.religionclause)
        if self.partyclause:
            content.append(self.partyclause)
        if self.autoqueryclause:
            content.append(self.autoqueryclause)
        if self.jubileeclause:
            content.append(self.jubileeclause)
        if self.directoryclause:
            content.append(self.directoryclause)
        if self.directmarketingclause:
            content.append(self.directmarketingclause)
        if self.militaryclause:
            content.append(self.militaryclause)
        if self.miscellaneousclause:
            content.append(self.miscellaneousclause)
        return content
