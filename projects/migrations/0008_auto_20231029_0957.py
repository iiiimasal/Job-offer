# Generated by Django 3.2.16 on 2023-10-29 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_company_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='certificate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='degree',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='job',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='telephone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
