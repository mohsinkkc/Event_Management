# Generated by Django 5.0 on 2023-12-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_service_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='sub_category',
            field=models.CharField(max_length=500, null=True),
        ),
    ]