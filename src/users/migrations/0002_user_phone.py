# Generated by Django 4.1.7 on 2023-03-17 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, max_length=50, null=True, verbose_name='Phone'),
        ),
    ]