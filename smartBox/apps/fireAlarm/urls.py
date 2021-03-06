from django.urls import path
from django.conf.urls import url
from .views import Api_FireAlarmMsg, Api_FireAlarmData, box_msg

app_name = 'fireAlarm'

urlpatterns = [
    # 火灾告警api
    # url('^api-box-data', Api_Box_FireAlarm.as_view()),
    url('^box_msg$', box_msg),

    url('^msg/$', Api_FireAlarmMsg.as_view()),
    url('^data/$', Api_FireAlarmData.as_view()),
]
