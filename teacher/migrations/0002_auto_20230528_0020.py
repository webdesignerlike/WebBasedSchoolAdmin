# Generated by Django 3.1.14 on 2023-05-27 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addressinfo',
            name='union',
        ),
        migrations.RemoveField(
            model_name='addressinfo',
            name='upazilla',
        ),
    ]
