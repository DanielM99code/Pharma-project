# Generated by Django 3.1.7 on 2021-04-19 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_pharma', '0017_auto_20210411_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',)},
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together={('id', 'slug')},
        ),
    ]
