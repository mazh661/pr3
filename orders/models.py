from django.db import models
from django.contrib.auth.models import User
from products.models import *
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return self.user.username+"->"+self.product.name