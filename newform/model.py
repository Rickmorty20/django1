from __future__ import unicode_literals
from django.db import models

class Registration(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('E', 'Erabi'),
    )

    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=20)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Date = models.DateTimeField(max_length=30)
    Age = models.IntegerField()
    upload = models.ImageField()

    class Meta:
        db_table = "student"
