from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.ContactForm)
admin.site.register(models.ViewLog)