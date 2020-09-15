# Generated by Django 3.0 on 2020-09-13 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Trabajadores', '0002_trabajadores_usuario'),
        ('Calificaciones', '0002_calificaciones_trabajador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificaciones',
            name='trabajador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='es_calificado', to='Trabajadores.Trabajadores'),
        ),
    ]