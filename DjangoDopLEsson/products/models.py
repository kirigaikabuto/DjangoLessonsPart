from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)#varchar sql
    description = models.TextField()#text sql
    price = models.IntegerField()#int sql

    def __str__(self):
        return self.name


# python manage.py makemigrations
# python manage.py migrate


