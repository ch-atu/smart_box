from django.db import models

# Create your models here.
from datetime import datetime


class Box_Inductor(models.Model):
    update_time = models.DateTimeField(verbose_name='更新时间', default=datetime.now)
    str_data = models.CharField(verbose_name='传感器数据', max_length=500)

    class Meta:
        db_table = 'db_Box_Inductor'
        verbose_name = '传感器API数据'
        verbose_name_plural = verbose_name


class InductorMsg(models.Model):
    INDUCTOR_STATUS = (
        (5, '网络离线'),
        (6, '设备离线'),
        (9, '正常'),
        (10, '告警'),
        (15, '正常'),
        (16, '告警'),
    )

    mac = models.CharField(verbose_name='云盒编码', max_length=30, blank=True, null=True)
    status = models.IntegerField(verbose_name='状态', choices=INDUCTOR_STATUS, default=6)
    type = models.IntegerField(blank=True, null=True)
    in1 = models.IntegerField(blank=True, null=True)
    in2 = models.IntegerField(blank=True, null=True)
    out1 = models.IntegerField(blank=True, null=True)
    out2 = models.IntegerField(blank=True, null=True)
    altert = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'db_InductorMsg'
        verbose_name = '传感器设备'
        verbose_name_plural = verbose_name


















