from django.db import models
import datetime

from campaigns.models import Campaign
# Create your models here.

class Reports(models.Model):
    createdAt = models.DateField(default=datetime.date.today)
    filepath = models.FileField(upload_to='uploads/%Y%m%d/')

    information_required = [
        ('bar chart spam filter', 'bar chart spam filter'),
        ('bar chart opened', 'bar chart opened'),
        ('bar chart clicked', 'bar chart clicked')
    ]

    information = models.CharField(max_length=55, choices=information_required, default='bar chart spam filter')
    id_campaing = models.ForeignKey(Campaign, on_delete=models.CASCADE)