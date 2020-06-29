from django.db import models
from janre.models import *


class Book(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    janre = models.ForeignKey(Janre,on_delete= models.CASCADE)

    def __str__(self):
        return self.name