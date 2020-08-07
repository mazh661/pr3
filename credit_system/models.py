from django.db import models
from products.models import *
from profiles.models import *
# Create your models here.
class Credit_category(models.Model):
    name = models.CharField(max_length=255)
    persent_per_year = models.IntegerField()
    number_of_month = models.IntegerField()
    def __str__(self):
        return self.name
        
class Credit(models.Model):
    credit_category = models.ForeignKey(Credit_category, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    accepted = models.BooleanField()