from django.core.mail import send_mail
from django.conf import settings
from accounts.models import MyUser

def sendemail(subject,message):
    userobjects = MyUser.objects.all()
    recipient_list = []
    for user in userobjects:
        recipient_list.append(user.email)
    email_from = settings.EMAIL_HOST_USER
    return send_mail( subject, message, email_from, recipient_list )