from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    product_name = models.CharField(max_length=255)
    amount = models.IntegerField()
    price = models.CharField(max_length=20)  
    description = models.TextField()
    brand = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

