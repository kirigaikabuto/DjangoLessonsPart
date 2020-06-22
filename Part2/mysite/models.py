from django.db import models


# create table Product (
# id serial pk,
# name varchar(255),
# price int
# );
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name
