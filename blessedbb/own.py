from pages import models
from django.core.mail import send_mail
from django.conf import settings
from accounts.models import MyUser
from blog.function import sendemail

def stores_ip(request):
    record = models.ViewLog(IP=request.geo_data.ip_address, city=request.geo_data.city,postal_code=request.geo_data.postal_code,country_name=request.geo_data.country_name,latitude=request.geo_data.latitude,is_unknown=request.geo_data.is_unknown)
    record.save()
    if models.ViewLog.objects.all().count() % 100 == 0:
        sendemail('You have scored another 100 views', f'Hey, you have recieved another 100 views and has a total views of {models.ViewLog.objects.all().count()}')

