# Generated by Django 4.0.8 on 2023-01-06 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='url',
            field=models.URLField(default='null'),
            preserve_default=False,
        ),
    ]