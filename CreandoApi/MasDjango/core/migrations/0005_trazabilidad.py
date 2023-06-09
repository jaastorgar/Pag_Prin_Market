# Generated by Django 4.2.1 on 2023-06-30 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_cliente_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trazabilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(verbose_name='Fecha de trazabilidad')),
                ('cantidad', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('accion', models.CharField(max_length=100, verbose_name='Acción realizada')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.productos')),
            ],
        ),
    ]
