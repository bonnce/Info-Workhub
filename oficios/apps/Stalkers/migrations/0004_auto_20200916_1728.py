# Generated by Django 3.0 on 2020-09-16 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calificaciones', '0002_calificaciones_trabajador'),
        ('Stalkers', '0003_stalkers_calificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stalkers',
            name='calificacion',
            field=models.ManyToManyField(blank=True, null=True, related_name='califica', to='Calificaciones.Calificaciones'),
        ),
    ]
