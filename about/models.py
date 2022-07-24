""" Imports required for models """
from django.db import models

class About(models.Model):
    """ Creates About table in db """
    class Meta:
        verbose_name = 'About'

    about_image = models.ImageField(null=True, blank=True)
    about_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name