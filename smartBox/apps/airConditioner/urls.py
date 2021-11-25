from django.urls import path
from .views import Api_AirConditioner, box_msg
from django.conf.urls import url

app_name = 'airConditioner'

urlpatterns = [
    # 获取空调数据API
    # url(r'^api-box-data/$', Api_Box_AirConditioner.as_view()),
    url(r'^box_msg$', box_msg),


    url(r'^air-cond/$', Api_AirConditioner.as_view()),
]
