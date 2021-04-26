# Generated by Django 3.1.1 on 2021-04-23 16:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0005_auto_20210423_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='campaign',
            name='finish_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Encerra em'),
        ),
        migrations.AddField(
            model_name='campaign',
            name='list',
            field=models.CharField(choices=[('Lista A', 'Lista A'), ('Lista B', 'Lista B'), ('Lista C', 'Lista C')], default='Lista A', max_length=12),
        ),
        migrations.AddField(
            model_name='campaign',
            name='start_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Inicia em'),
        ),
    ]