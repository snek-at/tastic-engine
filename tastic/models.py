from django.db import models
from django.contrib.auth.models import User


class Throughput(models.Model):
    date = models.DateTimeField(primary_key=True)
    requirements = models.IntegerField()
    features = models.IntegerField()
    opportunities = models.IntegerField()
    enhancements = models.IntegerField()
    bugs = models.IntegerField()


class BurnDown(models.Model):
    date = models.DateTimeField(primary_key=True)
    ideal = models.IntegerField()
    actual = models.IntegerField()


class Features(models.Model):
    filename = models.CharField(max_length=20, primary_key=True)
    date = models.DateTimeField(auto_now=True)
    path = models.CharField(max_length=200, null=True)


class Dods(models.Model):
    filename = models.CharField(max_length=20, primary_key=True)
    date = models.DateTimeField(auto_now=True)
    path = models.CharField(max_length=200, null=True)


class Stories(models.Model):
    filename = models.CharField(max_length=20, primary_key=True)
    date = models.DateTimeField(auto_now=True)
    path = models.CharField(max_length=200, null=True)

