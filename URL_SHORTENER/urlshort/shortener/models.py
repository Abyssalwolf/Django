from django.db import models

# Create your models here.

class Url(models.Model):
    original=models.CharField(max_length=500)
    short=models.CharField(max_length=300)
    custom=models.CharField(max_length=250)
    count=models.IntegerField(default=0)