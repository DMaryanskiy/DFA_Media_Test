# Generated by Django 4.1.6 on 2023-02-06 14:13

from django.db import migrations, models
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='image_url',
            field=models.ImageField(upload_to=gallery.models.upload_to),
        ),
    ]
