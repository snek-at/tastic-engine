from django.db import models

# Create your models here.

class BurnDown(models.Model):
    date = models.DateTimeField(primary_key=True)
    ideal = models.IntegerField()
    actual = models.IntegerField()
