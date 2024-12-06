from django.db import models

# Create your models here.
class community(models.Model):
    name = models.CharField(max_length=75)