from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    manager = models.CharField(max_length=100)
    # updated=models.DateTimeField(auto_now=True)
    # created=models.DateField(auto_now_add=True)
    
    # Optional: Define a string representation of the model
    def __str__(self):
        return self.name