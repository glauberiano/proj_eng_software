from django.db import models


class Campaign(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')