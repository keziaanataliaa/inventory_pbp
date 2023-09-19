from django.db import models

class Item(models.Model):
    product_name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.CharField(max_length=20)  
    description = models.TextField()
    brand = models.CharField(max_length=255)

