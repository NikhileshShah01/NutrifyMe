# Generated by Django 4.0.2 on 2022-04-03 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newproj', '0008_alter_registerdata_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerdata',
            name='userid',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True),
        ),
    ]