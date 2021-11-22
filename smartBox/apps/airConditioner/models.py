from datetime import datetime

from django.db import models

# Create your models here.


class AirConditionerData(models.Model):
    AIR_CONDITIONER_STATUS = [
        (1, '正常'),
        (2, '告警'),
        (5, '网络离线'),
        (6, '设备离线'),
        (15, '正常'),
    ]

    TEMP = [
        (1, '制冷'),
        (1, '制热')
    ]

    HUMIDITY = [
        (1, '除湿'),
        (2, '加湿'),
    ]

    status = models.CharField(verbose_name='状态', choices=AIR_CONDITIONER_STATUS, blank=True, null=True, max_length=10)
    preset_humidity = models.IntegerField(verbose_name='空调预设湿度', blank=True, null=True)
    discharge_pressure = models.IntegerField(verbose_name='排放压强', blank=True, null=True)
    actual_humidity = models.IntegerField(verbose_name='回风湿度', blank=True, null=True)
    fluid_temp_in = models.IntegerField(blank=True, null=True)
    net_status = models.IntegerField(verbose_name='网络状态', blank=True, null=True)
    altert = models.CharField(blank=True, null=True, max_length=50)
    cmp_drv_speed = models.IntegerField(blank=True, null=True)
    mac = models.CharField(verbose_name='云盒编码', blank=True, null=True, max_length=50)
    air_flow = models.IntegerField(blank=True, null=True)
    cool_dmd = models.IntegerField(blank=True, null=True)
    power_source = models.IntegerField(blank=True, null=True)
    rack_temp_3 = models.IntegerField(blank=True, null=True)
    cool_out = models.IntegerField(blank=True, null=True)
    rack_inlet_temp = models.IntegerField(blank=True, null=True)
    rack_temp_1 = models.IntegerField(blank=True, null=True)
    preset_temp = models.IntegerField(verbose_name='空调预设温度', blank=True, null=True)
    filter_dp = models.IntegerField(blank=True, null=True)
    supply_temp = models.IntegerField(blank=True, null=True)
    fluid_flow = models.IntegerField(blank=True, null=True)
    suction_pressure = models.IntegerField(blank=True, null=True)
    actual_temp = models.IntegerField(verbose_name='回风温度', blank=True, null=True)
    acfan = models.IntegerField(verbose_name='风机', blank=True, null=True)
    rack_temp_2 = models.IntegerField(blank=True, null=True)
    cmp_drv_coltage = models.IntegerField(blank=True, null=True)
    cmp_drv_power = models.IntegerField(blank=True, null=True)
    fluid_temp_out = models.IntegerField(blank=True, null=True)
    temp = models.CharField(verbose_name='制冷/制热', choices=TEMP, blank=True, null=True, max_length=10)
    fluid_valve_pos = models.IntegerField(blank=True, null=True)
    fan_speed = models.IntegerField(blank=True, null=True)
    humidity = models.CharField(verbose_name='除湿/加湿', choices=HUMIDITY, blank=True, null=True, max_length=10)
    update_time = models.DateTimeField(verbose_name='更新时间', default=datetime.now)

    class Meta:
        db_table = 'db_airConditionerData'
        verbose_name = "精密空调数据"
        verbose_name_plural = verbose_name


class Box_AirConditioner(models.Model):
    update_time = models.DateTimeField(verbose_name='更新时间', default=datetime.now)
    str_data = models.CharField(verbose_name='空调数据', max_length=500)

    class Meta:
        db_table = 'db_Box_AirConditioner'
        verbose_name = '空调api获取'
        verbose_name_plural = verbose_name



























