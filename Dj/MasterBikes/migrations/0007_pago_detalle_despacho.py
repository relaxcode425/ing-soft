# Generated by Django 5.0.6 on 2024-06-25 03:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterBikes', '0006_producto_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.AutoField(db_column='idPago', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('total', models.IntegerField()),
                ('metodo_pago', models.CharField(max_length=30)),
                ('domicilio', models.BooleanField()),
                ('rut', models.ForeignKey(db_column='rut', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id_detalle', models.AutoField(db_column='idDetalle', primary_key=True, serialize=False)),
                ('subtotal', models.IntegerField()),
                ('id_producto', models.ForeignKey(db_column='idProducto', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.producto')),
                ('id_pago', models.ForeignKey(db_column='idPago', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.pago')),
            ],
        ),
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id_despacho', models.AutoField(db_column='idDespacho', primary_key=True, serialize=False)),
                ('pedido', models.DateTimeField()),
                ('envio', models.DateTimeField()),
                ('recibo', models.DateTimeField()),
                ('id_pago', models.ForeignKey(db_column='idPago', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.pago')),
            ],
        ),
    ]
