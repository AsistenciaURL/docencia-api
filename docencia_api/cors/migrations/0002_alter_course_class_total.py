# Generated by Django 4.1.2 on 2022-11-02 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='class_total',
            field=models.IntegerField(default=0),
        ),
    ]