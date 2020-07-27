from django.db import models
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
    city = models.CharField(max_length=1000, null=True,blank=True)
    postal_code = models.CharField(max_length=1000, null=True,blank=True)
    country_name = models.CharField(max_length=1000, null=True,blank=True)
    latitude = models.CharField(max_length=1000, null=True,blank=True)
    longitude = models.CharField(max_length=1000, null=True,blank=True)
    is_unknown = models.BooleanField(default=False)

    def __str__(self):
        if self.is_unknown:
            return f'{self.IP}'
        else:
            return f'{self.IP} {self.country_name}'