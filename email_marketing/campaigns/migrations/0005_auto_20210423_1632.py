# Generated by Django 3.1.1 on 2021-04-23 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0004_auto_20210423_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='description',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='campaign',
            old_name='name',
            new_name='nome',
        ),
    ]
