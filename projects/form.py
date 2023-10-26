from django.forms import ModelForm
from .models import Company , Job
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']