from django.urls import path
from django.conf.urls import url
from .views import Api_HumitureEMsg, Api_HumitureSensorData, Api_HumitureThreshold, box_msg

app_name = 'humiture'

urlpatterns = [
    # 温湿度API
    # url('^api-box-data$', Api_Box_Humiture.as_view()),
    url('^box_msg$', box_msg),

    url('^EMsg/$', Api_HumitureEMsg.as_view()),
    url('^sensor/$', Api_HumitureSensorData.as_view()),
    url('^threshold/$', Api_HumitureThreshold.as_view()),
]
