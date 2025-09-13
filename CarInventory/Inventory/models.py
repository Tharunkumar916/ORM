from unittest.util import _MAX_LENGTH
from django.db import models
from django.forms import IntegerField

# Create your models here.
class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=40)
    year = models.DateField()
    price = models.IntegerField()
    type = models.CharField(max_length=10)

