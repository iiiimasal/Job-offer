from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.contrib.auth.models import AbstractUser

class normalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # company = models.ForeignKey('Company', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.user.username  

class Employer(models.Model):
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


# models.py
from django.db import models

class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    telephone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    manager = models.CharField(max_length=100)
    jobs = models.ManyToManyField(Job, related_name='company_jobs')
    participants = models.ManyToManyField(User, related_name='companies_participated_in')
    commercials = models.ManyToManyField('JobCommercial', related_name='companies_commercials', blank=True)

    def get_user_id(self):
        return self.user.id

    def __str__(self):
        return self.name


class JobCommercial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Jid = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    talents=models.TextField()
    description = models.TextField()
    date = models.DateField()
    companies = models.ManyToManyField('Company', related_name='commercials_companies', blank=True)

    def __str__(self):
        return self.subject



class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # Add this line
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50]





