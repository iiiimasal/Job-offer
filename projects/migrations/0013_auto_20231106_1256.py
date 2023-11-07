# Generated by Django 3.2.16 on 2023-11-06 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_auto_20231106_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='messages',
        ),
        migrations.RemoveField(
            model_name='company',
            name='participants',
        ),
        migrations.AddField(
            model_name='company',
            name='jobs',
            field=models.ManyToManyField(related_name='company_jobs', to='projects.Job'),
        ),
    ]
