# Generated by Django 4.2.1 on 2023-12-01 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_brand_brand_image_alter_event_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='barcode',
            name='barcode_number',
            field=models.TextField(default=''),
        ),
    ]
