# Generated by Django 2.2.10 on 2021-11-18 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airConditioner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airconditionerdata',
            name='humidity',
            field=models.CharField(blank=True, choices=[(1, '除湿'), (2, '加湿')], default=1, max_length=10, null=True, verbose_name='除湿/加湿'),
        ),
        migrations.AlterField(
            model_name='airconditionerdata',
            name='status',
            field=models.CharField(blank=True, choices=[(1, '正常'), (2, '告警'), (5, '网络离线'), (6, '设备离线'), (15, '正常')], max_length=10, null=True, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='airconditionerdata',
            name='temp',
            field=models.CharField(blank=True, choices=[(1, '制冷'), (1, '制热')], default=1, max_length=10, null=True, verbose_name='制冷/制热'),
        ),
    ]
