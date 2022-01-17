from django.db import models

class Merop(models.Model):
    name = models.CharField(max_length=200, blank=False, default='')
    participants = models.CharField(max_length=200, blank=False, default='')
    date = models.CharField(max_length=200, blank=False, default='')
    place = models.CharField(max_length=200, blank=False, default='')
    description = models.TextField(max_length=2000, blank=False, default='')
    published = models.BooleanField(default=False)
