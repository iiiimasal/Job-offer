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
        fields =  ['user','name', 'email', 'telephone_number', 'manager','city']

class NormalUserForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    is_employer = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    is_employee = forms.BooleanField(required=False, widget=forms.CheckboxInput)