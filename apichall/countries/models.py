from django.db import models

# Create your models here.
class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    countryCode = models.CharField(max_length=3)
    createdAt = models.DateTimeField(auto_now_add=True)
    groupId = models.IntegerField(default=0)