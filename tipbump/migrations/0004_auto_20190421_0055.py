# Generated by Django 2.2 on 2019-04-21 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tipbump', '0003_auto_20190421_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=200)),
                ('store_id', models.CharField(max_length=50)),
                ('report_creation_day', models.CharField(blank=True, max_length=50, null=True)),
                ('report_creation_time', models.DateTimeField()),
                ('report_emails', models.CharField(blank=True, max_length=1000, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.DeleteModel(
            name='Location',
        ),
    ]
