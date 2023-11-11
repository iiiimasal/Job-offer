# projects/utils.py

from django.contrib.auth.models import User
from django.contrib.auth.models import Group

def create_user(username, email, password, is_employer=False, is_employee=False):
    user = User.objects.create_user(username=username, email=email, password=password)

    if is_employer:
        employer_group, created = Group.objects.get_or_create(name='Employers')
        user.groups.add(employer_group)
    elif is_employee:
        employee_group, created = Group.objects.get_or_create(name='Employees')
        user.groups.add(employee_group)

    return user
