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

class EmployerRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address')
    telephone_number = forms.CharField(max_length=15)
    # gender = forms.CharField(max_length=10)
    city = forms.CharField(max_length=50)
    certificate = forms.CharField(max_length=100)
    degree = forms.CharField(max_length=50)
    age = forms.IntegerField()
    job = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    # Add a field to choose the role
    is_employer = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    is_employee = forms.BooleanField(required=False, widget=forms.CheckboxInput)
