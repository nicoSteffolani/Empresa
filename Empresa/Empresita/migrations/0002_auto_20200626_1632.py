# Generated by Django 2.2 on 2020-06-26 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Empresita', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='venta',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='monto_final',
        ),
        migrations.AddField(
            model_name='venta',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Empresita.Cliente'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='descuento',
            field=models.BooleanField(null=True),
        ),
    ]
