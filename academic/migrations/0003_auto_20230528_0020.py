# Generated by Django 3.1.14 on 2023-05-27 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_auto_20200128_1231'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='classregistration',
            unique_together={('class_name', 'section', 'shift')},
        ),
        migrations.RemoveField(
            model_name='classregistration',
            name='guide_teacher',
        ),
        migrations.DeleteModel(
            name='GuideTeacher',
        ),
    ]
