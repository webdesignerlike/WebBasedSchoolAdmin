# Generated by Django 3.1.14 on 2023-05-28 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20230528_0020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobinfo',
            name='first_time_scale_due_year',
        ),
        migrations.RemoveField(
            model_name='jobinfo',
            name='recreation_leave_due_year',
        ),
        migrations.RemoveField(
            model_name='jobinfo',
            name='second_time_scale_due_year',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='driving_license_passport',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='e_tin',
        ),
        migrations.RemoveField(
            model_name='personalinfo',
            name='nid',
        ),
    ]