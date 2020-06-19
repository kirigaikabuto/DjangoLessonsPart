from django.db import models


# create table Product (
#   pk serial primary key,

class Product(models.Model):
    # name varchar(255),
    name = models.CharField(max_length=255)
    # price int
    price = models.IntegerField()

    def __str__(self):
        return self.name
