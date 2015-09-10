from django.db import models

# Create your models here.

class Author(models.Model):
    gender = models.CharField(max_length=7)
    age = models.PositiveSmallIntegerField()
    predictedGender = models.CharField(max_length=7,null=True)
    predictedAge = models.PositiveSmallIntegerField(null=True)
    date = models.DateTimeField("Date requested")

    def __str__(self):              # __unicode__ on Python 2
        pass