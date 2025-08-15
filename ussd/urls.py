
from django.urls import path
from .views import sms_callback
from .views import ussd_callback


urlpatterns = [
    path('ussd/', ussd_callback, name='ussd_cLlback'),
     path('sms/', sms_callback, name='sms_callback'),
]