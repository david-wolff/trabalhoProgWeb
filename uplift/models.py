from django.db import models

class Lift(models.Model):
    # define your fields here
    driver = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    # add other necessary fields
