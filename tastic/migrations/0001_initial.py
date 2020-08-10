# Generated by Django 3.0.8 on 2020-08-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BurnDown',
            fields=[
                ('date', models.DateTimeField(primary_key=True, serialize=False)),
                ('ideal', models.IntegerField()),
                ('actual', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Throughput',
            fields=[
                ('date', models.DateTimeField(primary_key=True, serialize=False)),
                ('requirements', models.IntegerField()),
                ('features', models.IntegerField()),
                ('opportunities', models.IntegerField()),
                ('enchancements', models.IntegerField()),
                ('bugs', models.IntegerField()),
            ],
        ),
    ]
