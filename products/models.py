from django.db import models


class Product(models.Model):
    productid = models.IntegerField()
    productname = models.CharField(max_length=50)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

class Offers(models.Model):
    offerid = models.IntegerField()
    offercode = models.CharField(max_length=20)
    offerdescription = models.CharField(max_length=250)
    offerdiscount = models.FloatField()
