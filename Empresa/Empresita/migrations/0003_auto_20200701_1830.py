# Generated by Django 2.2 on 2020-07-01 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empresita', '0002_auto_20200626_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='descuento',
            field=models.FloatField(null=True),
        ),
    ]
