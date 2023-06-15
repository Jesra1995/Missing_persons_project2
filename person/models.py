from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length= 25)
    last_name = models.CharField(max_length=25) 
    date_missing = models.DateField
    age_at_missing = models.IntegerField
    city = models.CharField(max_length= 20)
    state = models.CharField(max_length=2)
    gender = models.CharField(max_length=1)
    race = models.CharField(max_length= 20)
