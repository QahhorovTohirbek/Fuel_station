# Generated by Django 5.0.6 on 2024-05-15 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='fuel',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]