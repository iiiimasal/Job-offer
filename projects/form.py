from django.forms import ModelForm
from .models import Company , Job , Employer ,Employee ,JobCommercial
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
        exclude=['user','participants','jobs','commercials']
        # fields =  ['user','name', 'email', 'telephone_number', 'manager','city']

class NormalUserForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    is_employer = forms.BooleanField(required=False, widget=forms.CheckboxInput)
    is_employee = forms.BooleanField(required=False, widget=forms.CheckboxInput)


class EmployerRegistrationForm(ModelForm):
    class Meta:
        model = Employer
        fields =  ['user','telephone_number', 'gender', 'certificate', 'degree','age','city','job']

class EmployeeRegistrationForm(ModelForm):
    class Meta:
        model = Employee
        fields =  ['user','telephone_number', 'gender', 'certificate', 'degree','age','city','job']


class JobCommercialForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(JobCommercialForm, self).__init__(*args, **kwargs)
        # Filter the queryset for the companies field based on the user
        self.fields['companies'].queryset = Company.objects.filter(user=user)

    companies = forms.ModelMultipleChoiceField(
        queryset=Company.objects.none(),  # Initially, an empty queryset
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = JobCommercial
        fields = ['subject', 'talents', 'description', 'date', 'companies']
