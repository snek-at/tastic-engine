# Generated by Django 3.0.8 on 2020-08-12 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tastic', '0002_auto_20200810_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dods',
            fields=[
                ('filename', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('download_url', models.URLField()),
                ('view_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('filename', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('download_url', models.URLField()),
                ('view_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Stories',
            fields=[
                ('filename', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('download_url', models.URLField()),
                ('view_url', models.URLField()),
            ],
        ),
    ]
