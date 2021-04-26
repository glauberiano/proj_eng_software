from django.db import models
import datetime


class Campaign(models.Model):
    status_choice = [
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled')
    ]
    contacts_choice = [
        ('List A', 'List A'),
        ('List B', 'List B'),
        ('List C', 'List C'),
    ]
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=255)
    start_date = models.DateField('Start Date', default=datetime.date.today)
    finish_date = models.DateField('Finish Date', default=datetime.date.today)
    status = models.CharField(max_length=12, choices=status_choice, default='Completed')
    list = models.CharField(max_length=12, choices=contacts_choice, default='List A')
    email_body = models.TextField(help_text='Write your email here', default='Ola')



