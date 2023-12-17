# Generated by Django 5.0 on 2023-12-16 04:18

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AccommodationHireApp', '0003_alter_user_avatar_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar_user',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
