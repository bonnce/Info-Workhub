# Generated by Django 3.0 on 2020-09-11 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='Trabajador',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='phone',
            field=models.BigIntegerField(null=True),
        ),
    ]
