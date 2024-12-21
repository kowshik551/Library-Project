from django.db import models

# Create your models here.

class books(models.Model):

    Book_Title = models.CharField(max_length=200)
    Author_Name = models.CharField(max_length=100)
    Year = models.IntegerField()
    Genre = models.CharField(max_length=100)



