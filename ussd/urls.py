
from django.urls import path
from .views import sms_callback


urlpatterns = [
    path('ussd/', sms_callback, name='ussd'),
     path('sms/', sms_callback, name='sms_callback'),
]