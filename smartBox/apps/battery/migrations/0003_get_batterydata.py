# Generated by Django 2.2.10 on 2021-11-22 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battery', '0002_auto_20211117_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Get_BatteryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')),
                ('str_data', models.CharField(max_length=500, verbose_name='电池数据')),
            ],
        ),
    ]