# Generated by Django 5.0.7 on 2025-01-31 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project1', '0004_remove_department_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='department',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
