from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone





class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    certificate = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    age = models.IntegerField()
    job = models.CharField(max_length=100)

    # Add other custom fields here

    def __str__(self):
        return self.user.username


class Job(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()


# Define the Company model
class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    manager = models.CharField(max_length=100)
    jobs = models.ManyToManyField(Job, related_name='company_jobs')  # Reference the Job model
    participants = models.ManyToManyField(User, related_name='companies_participated_in')
    # Add other fields and methods as needed

    def get_user_id(self):
        return self.user.id

    def __str__(self):
        return self.name
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)
    telephone_number = models.CharField(max_length=15, null=True, blank=True)
    # gender = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    certificate = models.CharField(max_length=100, null=True, blank=True)
    degree = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    job = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username    

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)
    telephone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    certificate = models.CharField(max_length=100, null=True, blank=True)
    degree = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    job = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username    


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # Add this line
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]
