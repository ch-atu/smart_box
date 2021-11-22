from django.db import models

# Create your models here.
from datetime import datetime


class Box_FireAlarm(models.Model):
    update_time = models.DateTimeField(verbose_name='更新时间', default=datetime.now)
    str_data = models.CharField(verbose_name='火灾告警数据', max_length=500)

    class Meta:
        db_table = 'db_Box_FireAlarm'
        verbose_name = '火灾告警api获取'


class FireAlarmMessage(models.Model):
    altert = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(verbose_name='型号', max_length=50, blank=True, null=True)
    status = models.IntegerField(verbose_name='状态', blank=True, null=True)
    protocol = models.CharField(max_length=50, verbose_name='协议', blank=True, null=True)

    class Meta:
        db_table = 'db_fireAlarmMessage'
        verbose_name = "电气火灾设备基本信息"
        verbose_name_plural = verbose_name


class FireAlarmData(models.Model):
    RELEASE_STATUS = (
        (0, '关'),
        (1, '开')
    )

    MACHINE_STATUS = (
        (15, '正常'),
        (16, '告警'),
    )

    box_id = models.CharField(verbose_name='盒子id', max_length=50, blank=True, null=True)
    volt_a = models.FloatField(verbose_name='电压A相', blank=True, null=True)
    volt_b = models.FloatField(verbose_name='电压B相', blank=True, null=True)
    volt_c = models.FloatField(verbose_name='电压C相', blank=True, null=True)
    current_a = models.FloatField(verbose_name='电流A相', blank=True, null=True)
    current_b = models.FloatField(verbose_name='电流B相', blank=True, null=True)
    current_c = models.FloatField(verbose_name='电流C相', blank=True, null=True)
    current_l = models.FloatField(verbose_name='漏电流', blank=True, null=True)
    temp_a = models.FloatField(verbose_name='温度A相', blank=True, null=True)
    temp_b = models.FloatField(verbose_name='温度B相', blank=True, null=True)
    temp_c = models.FloatField(verbose_name='温度C相', blank=True, null=True)
    temp_l = models.FloatField(verbose_name='温度L相', blank=True, null=True)
    temp_n = models.FloatField(verbose_name='温度N相', blank=True, null=True)
    power_a = models.FloatField(verbose_name='功率A相', blank=True, null=True)
    power_b = models.FloatField(verbose_name='功率B相', blank=True, null=True)
    power_c = models.FloatField(verbose_name='功率C相', blank=True, null=True)
    pfa = models.FloatField(verbose_name='功率因数A相', blank=True, null=True)
    pfb = models.FloatField(verbose_name='功率因数B相', blank=True, null=True)
    pfc = models.FloatField(verbose_name='功率因数C相', blank=True, null=True)
    release_status = models.IntegerField(verbose_name='脱扣器状态', choices=RELEASE_STATUS, blank=True, null=True)
    power_wh = models.FloatField(verbose_name='电镀', blank=True, null=True)
    status = models.IntegerField(verbose_name='机器状态', choices=MACHINE_STATUS, blank=True, null=True)
    fire_alarm_message = models.ForeignKey('FireAlarmMessage', on_delete=models.CASCADE)
    update_time = models.DateTimeField(verbose_name='数据更新时间', default=datetime.now)


    class Meta:
        db_table = 'db_FireAlarmData'
        verbose_name = "电气火灾设备数据"
        verbose_name_plural = verbose_name






