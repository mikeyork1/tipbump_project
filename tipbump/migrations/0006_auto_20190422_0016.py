# Generated by Django 2.2 on 2019-04-22 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tipbump', '0005_auto_20190421_1309'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SiteConfiguration',
            new_name='Site',
        ),
    ]