# Generated by Django 4.1.2 on 2022-11-03 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cors', '0005_alter_qr_limit_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='qr',
            name='init_date',
            field=models.DateTimeField(default='2008-11-11 13:23:44'),
            preserve_default=False,
        ),
    ]
