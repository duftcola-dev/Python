# Generated by Django 4.1.1 on 2022-10-03 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online_store', '0002_alter_empleado_options_alter_manager_options_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tienda',
            unique_together={('nombre_tienda', 'manager')},
        ),
    ]
