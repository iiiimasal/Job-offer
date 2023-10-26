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

class EmployeeRegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    # Add a field to choose the role
    is_employee = forms.BooleanField(required=False, widget=forms.CheckboxInput)