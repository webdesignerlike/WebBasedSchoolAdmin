# Generated by Django 3.1.14 on 2023-05-28 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0015_auto_20230528_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicinfo',
            name='registration_no',
            field=models.IntegerField(default=141664, unique=True),
        ),
    ]
