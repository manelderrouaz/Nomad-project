# Generated by Django 4.1.7 on 2023-05-03 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='Specification',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
