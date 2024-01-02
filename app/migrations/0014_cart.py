# Generated by Django 5.0 on 2023-12-19 12:06

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rent_image_alter_rent_date_end_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
                ('rent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.rent')),
            ],
        ),
    ]