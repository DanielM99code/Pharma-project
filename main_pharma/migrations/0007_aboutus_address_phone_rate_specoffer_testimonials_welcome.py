# Generated by Django 3.1.7 on 2021-04-08 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_pharma', '0006_auto_20210408_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(default='SOME STRING', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=20)),
                ('street', models.CharField(max_length=20)),
                ('home', models.CharField(max_length=5)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, unique=True)),
                ('photo', models.ImageField(upload_to='rate/%Y/%m/%d')),
                ('desc', models.CharField(default='SOME STRING', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpecOffer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, unique=True)),
                ('desc', models.CharField(default='SOME STRING', max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('quote', models.CharField(default='SOME STRING', max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='testimonials/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Welcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15, unique=True)),
                ('photo', models.ImageField(upload_to='welcome/%Y/%m/%d')),
                ('desc', models.CharField(default='SOME STRING', max_length=200, unique=True)),
            ],
        ),
    ]
