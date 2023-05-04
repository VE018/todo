from django.db import models

# Create your models here.
class todays(models.Model):
    index = models.CharField(max_length=500)
    task = models.CharField(max_length=200)



