# Generated by Django 4.0.5 on 2022-07-01 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0006_booked_tour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked_tour',
            name='tour_slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]