from django.urls import path
from django.conf.urls import url

from .views import box_msg

app_name = 'inductor'

urlpatterns = [
    # 传感器API
    # url(r'^api-box-data/$', API_Box_Inductor.as_view()),
    url(r'^box_msg$', box_msg),
]
