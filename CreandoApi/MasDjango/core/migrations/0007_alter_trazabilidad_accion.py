# Generated by Django 4.2.1 on 2023-06-30 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_trazabilidad_accion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trazabilidad',
            name='accion',
            field=models.CharField(max_length=100, verbose_name='Acción realizada'),
        ),
    ]