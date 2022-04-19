# Generated by Django 4.0.4 on 2022-04-18 23:52

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('neighbourhood', '0003_rename_neighborhood_profile_neighbourhood_business'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='picture',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
    ]