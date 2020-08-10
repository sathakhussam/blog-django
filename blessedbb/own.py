from pages import models
from django.core.mail import send_mail
from django.conf import settings
from accounts.models import MyUser
from blog.function import sendemail

def stores_ip(request):
    record = models.ViewLog(IP=get_client_ip(request))
    record.save()
    if models.ViewLog.objects.all().count() % 100 == 0:
        sendemail('You have scored another 100 views', f'Hey, you have recieved another 100 views and has a total views of {models.ViewLog.objects.all().count()}')
    # pass
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip