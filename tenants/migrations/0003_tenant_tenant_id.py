# Generated by Django 3.1 on 2020-08-18 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='tenant_id',
            field=models.SlugField(blank=True),
        ),
    ]
