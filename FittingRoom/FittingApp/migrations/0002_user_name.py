# Generated by Django 2.0 on 2020-01-19 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FittingApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='Please enter your name', max_length=30),
        ),
    ]