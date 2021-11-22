from django.urls import path
from django.conf.urls import url

from .views import API_Box_Inductor

app_name = 'inductor'

urlpatterns = [
    # 传感器API
    url(r'^api-box-data/$', API_Box_Inductor.as_view()),
]
