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


class Job (models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    # updated=models.DateTimeField(auto_now=True)
    # created=models.DateField(auto_now_add=True)

    # class Meta:
    # ###the newest are the last
    # # ordering=['updated','created']
    # ###the newest are the first
    #  ordering=['-updated','-created']
    # Optional: Define a string representation of the model
    def __str__(self):
        return self.title
class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)
    # Add other fields specific to employees
    # For example, you can add fields like employee_name, employee_email, etc.

    def __str__(self):
        return self.user.username    