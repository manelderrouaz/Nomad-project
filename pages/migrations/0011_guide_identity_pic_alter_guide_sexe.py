# Generated by Django 4.1.7 on 2023-04-23 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_guide_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='guide',
            name='identity_pic',
            field=models.ImageField(blank=True, null=True, upload_to='identity_pics/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='guide',
            name='sexe',
            field=models.CharField(choices=[('femme', 'femme'), ('homme', 'homme')], max_length=50),
        ),
    ]
