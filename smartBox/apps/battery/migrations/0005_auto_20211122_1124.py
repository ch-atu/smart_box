# Generated by Django 2.2.10 on 2021-11-22 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('battery', '0004_auto_20211122_1012'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Get_BatteryData',
            new_name='Box_Battery',
        ),
        migrations.AlterModelTable(
            name='box_battery',
            table='db_Box_Battery',
        ),
    ]
