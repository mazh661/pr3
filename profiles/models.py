from django.db import models
from django.contrib.auth.models import User
class Department(models.Model):
    name = models.CharField(max_length=255)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    salary = models.IntegerField()

    def __str__(self):
        return self.user.username