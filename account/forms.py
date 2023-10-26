from django.db import models
from django.contrib.auth.models import User

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'