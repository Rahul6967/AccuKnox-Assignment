# Generated by Django 4.2.13 on 2024-09-14 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.CharField(default='Active', max_length=100),
        ),
    ]