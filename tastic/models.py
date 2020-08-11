from django.db import models


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
