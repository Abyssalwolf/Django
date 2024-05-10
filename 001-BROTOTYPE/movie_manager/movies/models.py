from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=200)
    sub=models.CharField(max_length=500)
    sum=models.TextField()