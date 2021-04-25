# Generated by Django 3.1.7 on 2021-04-07 20:15

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('main_pharma', '0003_auto_20210407_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_full',
            field=models.ImageField(blank=True, upload_to='products/full/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_small',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=0, size=[270, 370], upload_to='products/small/%Y/%m/%d'),
        ),
    ]
