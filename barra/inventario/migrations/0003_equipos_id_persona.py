# Generated by Django 2.0 on 2018-02-01 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20180129_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipos',
            name='id_persona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventario.Personas'),
        ),
    ]
