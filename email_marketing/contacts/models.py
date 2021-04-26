from django.db import models

# Create your models here.
class Contacts(models.Model):
    email = models.EmailField(unique=True)