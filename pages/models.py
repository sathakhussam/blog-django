from django.db import models
from django.utils import timezone
from blessedbb.own import sendemail
# Create your models here.
class ContactForm(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'{self.name} ({self.email})'

class ViewLog(models.Model):
    IP = models.CharField(max_length=150)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f'{self.IP}'