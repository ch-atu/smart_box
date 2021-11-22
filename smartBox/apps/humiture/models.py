from django.db import models

# Create your models here.
from datetime import datetime


class Box_Humiture(models.Model):
    update_time = models.DateTimeField(verbose_name='更新时间', default=datetime.now)
    str_data = models.CharField(verbose_name='温湿度数据', max_length=500)

    class Meta:
        db_table = 'db_Box_Humiture'
        verbose_name = '温湿度API数据'
        verbose_name_plural = verbose_name


class HumitureEquipmentMsg(models.Model):
    HUMITURE_STATUS = (
        (5, '网络离线'),
        (6, '设备离线'),
        (7, '正常'),
        (8, '告警'),
        (15, '正常'),
        (16, '告警'),
    )

    master = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(verbose_name='状态', choices=HUMITURE_STATUS, default=6)
    protocol = models.CharField(verbose_name='协议', max_length=50, blank=True, null=True)
    altert = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'db_HumitureEquipmentMsg'
        verbose_name = "温湿度设备信息"
        verbose_name_plural = verbose_name


class HumitureSensorData(models.Model):
    order_id = models.IntegerField(verbose_name='温湿度序号', blank=True, null=True)
    status = models.IntegerField(verbose_name='状态', blank=True, null=True)
    temp = models.FloatField(verbose_name='温度', blank=True, null=True)
    mac = models.CharField(verbose_name='云盒编码', max_length=50, blank=True, null=True)
    humidity = models.FloatField(verbose_name='湿度', blank=True, null=True)
    device_name = models.CharField(verbose_name='设备名称', max_length=20, blank=True, null=True)
    altert = models.CharField(max_length=50, blank=True, null=True)
    device_id = models.CharField(verbose_name='设备序号', max_length=10, blank=True, null=True)
    update_time = models.DateTimeField(verbose_name='更新时间', default=datetime.now)
    humiture_equipment_msg = models.ForeignKey('HumitureEquipmentMsg', on_delete=models.CASCADE)

    class Meta:
        db_table = 'db_HumitureSensorData'
        verbose_name = '温湿度传感器数据'
        verbose_name_plural = verbose_name


class HumitureThreshold(models.Model):
    temp_la = models.IntegerField(blank=True, null=True)
    temp_lr = models.IntegerField(blank=True, null=True)
    temp_ha = models.IntegerField(blank=True, null=True)
    temp_hr = models.IntegerField(blank=True, null=True)
    humidity_la = models.IntegerField(blank=True, null=True)
    humidity_lr = models.IntegerField(blank=True, null=True)
    humidity_ha = models.IntegerField(blank=True, null=True)
    humidity_hr = models.IntegerField(blank=True, null=True)
    box_id = models.CharField(verbose_name='盒子序号', max_length=20, blank=True, null=True)
    device_id = models.CharField(verbose_name='设备序号', max_length=30, blank=True, null=True)
    update_time = models.DateTimeField(verbose_name='更新时间', default=datetime.now)

    class Meta:
        db_table = 'db_HumitureThreshold'
        verbose_name = '温湿度阈值'
        verbose_name_plural = verbose_name





















