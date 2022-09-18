# Generated by Django 4.0.2 on 2022-04-02 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newproj', '0004_alter_registerdata_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerdata',
            name='id',
        ),
        migrations.AlterField(
            model_name='registerdata',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], max_length=10),
        ),
        migrations.AlterField(
            model_name='registerdata',
            name='userid',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]