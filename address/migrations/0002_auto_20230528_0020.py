# Generated by Django 3.1.14 on 2023-05-27 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20230528_0020'),
        ('teacher', '0002_auto_20230528_0020'),
        ('student', '0014_auto_20230528_0020'),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upazilla',
            name='district',
        ),
        migrations.DeleteModel(
            name='Union',
        ),
        migrations.DeleteModel(
            name='Upazilla',
        ),
    ]