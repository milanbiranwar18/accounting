# Generated by Django 5.0.2 on 2024-02-28 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_student'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='UserLog',
        ),
    ]
