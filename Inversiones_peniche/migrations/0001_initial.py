# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-20 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuota', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Inversiones_peniche.Cuota')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('apellido', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frecuencia_pago', models.CharField(max_length=30)),
                ('cuotas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inversiones_peniche.Cuota')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=40, unique=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inversiones_peniche.Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Inversiones_peniche.Persona')),
            ],
            bases=('Inversiones_peniche.persona',),
        ),
        migrations.CreateModel(
            name='Operador',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Inversiones_peniche.Persona')),
            ],
            bases=('Inversiones_peniche.persona',),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Inversiones_peniche.Persona')),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=30)),
                ('password_salt', models.CharField(max_length=30)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inversiones_peniche.Rol')),
            ],
            bases=('Inversiones_peniche.persona',),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='vehiculo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Inversiones_peniche.Vehiculo'),
        ),
        migrations.AddField(
            model_name='persona',
            name='Telefonos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inversiones_peniche.Telefono'),
        ),
        migrations.AddField(
            model_name='factura',
            name='prestamo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Inversiones_peniche.Prestamo'),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='operador',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Inversiones_peniche.Operador'),
        ),
        migrations.AddField(
            model_name='factura',
            name='cliente',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Inversiones_peniche.Cliente'),
        ),
        migrations.AddField(
            model_name='factura',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Inversiones_peniche.Operador'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='prestamo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inversiones_peniche.Prestamo'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='vehiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inversiones_peniche.Vehiculo'),
        ),
    ]
