# Generated by Django 2.2.4 on 2019-10-17 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erpe', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informe',
            old_name='informe_text',
            new_name='Domicilio_Instalacion',
        ),
        migrations.RemoveField(
            model_name='informe',
            name='Domicilio',
        ),
        migrations.RemoveField(
            model_name='informe',
            name='Fecha',
        ),
        migrations.RemoveField(
            model_name='informe',
            name='Nombre',
        ),
        migrations.RemoveField(
            model_name='informe',
            name='Pendientes',
        ),
        migrations.AddField(
            model_name='informe',
            name='Nombre_Apellido',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='informe',
            name='informe_Producto',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
