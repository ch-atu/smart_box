from django.db import models

# Create your models here.

from datetime import datetime


class Box_Battery(models.Model):
    update_time = models.DateTimeField(verbose_name='更新时间', default=datetime.now)
    str_data = models.CharField(verbose_name='电池数据', max_length=500)

    class Meta:
        db_table = 'db_Box_Battery'
        verbose_name = '电池数据'
        verbose_name_plural = verbose_name


class BatteryMessage(models.Model):
    volt = models.IntegerField(verbose_name='单节电池电压', blank=True, null=True)
    volt1 = models.IntegerField(verbose_name='单节电池电压1', blank=True, null=True)
    volt2 = models.IntegerField(verbose_name='单节电池电压2', blank=True, null=True)
    volt3 = models.IntegerField(verbose_name='单节电池电压3', blank=True, null=True)
    volt4 = models.IntegerField(verbose_name='单节电池电压4', blank=True, null=True)
    tmpture1 = models.FloatField(verbose_name='单节电池温度1', blank=True, null=True)
    tmpture2 = models.FloatField(verbose_name='单节电池温度2', blank=True, null=True)
    temp = models.FloatField(verbose_name='单节电池温度', blank=True, null=True)
    current = models.FloatField(verbose_name='电流', blank=True, null=True)
    resistance = models.FloatField(verbose_name='单节电池电阻', blank=True, null=True)
    bat_status = models.IntegerField(verbose_name='状态', blank=True, null=True)
    mac = models.CharField(blank=True, null=True, max_length=50)
    altert = models.CharField(blank=True, null=True, max_length=50)
    status = models.IntegerField(blank=True, null=True)
    cell_altert = models.CharField(blank=True, null=True, max_length=50)
    order_id = models.IntegerField(blank=True, null=True)
    device_id = models.IntegerField(blank=True, null=True)
    battery_state = models.ForeignKey('BatteryState', on_delete=models.CASCADE)
    update_time = models.DateTimeField(verbose_name='更新时间', default=datetime.now, blank=True, null=True)

    class Meta:
        db_table = 'db_BatteryMessage'
        verbose_name = "电池基本信息"
        verbose_name_plural = verbose_name


class BatteryState(models.Model):
    STATE_LIST = (
        (5, '网络离线'),
        (6, '设备离线'),
        (11, '正常'),
        (12, '告警'),
        (15, '正常'),
        (16, '告警'),

    )
    altert = models.CharField(blank=True, null=True, max_length=50)
    master = models.IntegerField(blank=True, null=True)
    current = models.FloatField(verbose_name='电流', blank=True, null=True)
    agent = models.IntegerField(verbose_name='代理', blank=True, null=True)
    status = models.IntegerField(verbose_name='状态', choices=STATE_LIST, default=6)
    temp = models.FloatField(verbose_name='环境温度', blank=True, null=True)
    volt = models.FloatField(verbose_name='总电压', blank=True, null=True)
    cloud_alarm = models.ForeignKey('CloudAlarm', on_delete=models.CASCADE)

    class Meta:
        db_table = 'db_BatteryState'
        verbose_name = "电池基本状态"
        verbose_name_plural = verbose_name


class CloudAlarm(models.Model):
    temp_lr = models.IntegerField(verbose_name='低温解除阈值', blank=True, null=True)
    temp_hr = models.IntegerField(verbose_name='高温解除阈值', blank=True, null=True)
    temp_la = models.IntegerField(verbose_name='低温告警阈值', blank=True, null=True)
    temp_ha = models.IntegerField(verbose_name='高温告警阈值', blank=True, null=True)
    volt_la = models.FloatField(verbose_name='欠压告警阈值', blank=True, null=True)
    volt_hr = models.FloatField(verbose_name='过压解除阈值', blank=True, null=True)
    volt_lr = models.FloatField(verbose_name='欠压解除阈值', blank=True, null=True)
    volt_ha = models.FloatField(verbose_name='过压告警阈值', blank=True, null=True)
    current_detection = models.IntegerField(verbose_name='电流检测', blank=True, null=True)
    curr_ratio = models.IntegerField(verbose_name='电流比率', blank=True, null=True)
    resistance_hr = models.IntegerField(verbose_name='内阻高解除阈值', blank=True, null=True)
    resistance_ha = models.IntegerField(verbose_name='内阻高告警阈值', blank=True, null=True)
    bat_group_num = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'db_CloudAlarm'
        verbose_name = "云系统告警阈值"
        verbose_name_plural = verbose_name


