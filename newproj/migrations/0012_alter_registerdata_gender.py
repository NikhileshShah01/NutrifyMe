# Generated by Django 4.0.2 on 2022-04-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newproj', '0011_alter_registerdata_height_alter_registerdata_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerdata',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]