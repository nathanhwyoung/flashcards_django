# Generated by Django 4.0.8 on 2023-03-03 23:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0014_userprogress_times_seen'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Site',
            new_name='WebSite',
        ),
    ]
