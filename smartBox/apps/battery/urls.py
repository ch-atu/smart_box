from django.urls import path
from django.conf.urls import url
from .views import Api_BatteryMsg, Api_BatterySta, Api_BatteryAlarm, Api_Box_Battery

app_name = 'battery'

urlpatterns = [
    # 获取电池数据API
    url(r'^api-box-data/$', Api_Box_Battery.as_view()),


    url(r'^msg/$', Api_BatteryMsg.as_view()),
    url(r'^sta/$', Api_BatterySta.as_view()),
    url(r'^alarm/$', Api_BatteryAlarm.as_view()),
]
