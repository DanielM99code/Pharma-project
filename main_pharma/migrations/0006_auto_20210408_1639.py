# Generated by Django 3.1.7 on 2021-04-08 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pharma', '0005_product_is_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
