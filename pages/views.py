from django.contrib.gis.geoip2 import GeoIP2
from django.shortcuts import render
from . import forms
from blog import models
from blessedbb.own import stores_ip
from blog.function import sendemail

# Create your views here.
def home(requests):
    stores_ip(requests)
    objs = models.BlogPost.objects.filter(is_published=True)
    return render(requests, 'pages/home.html',{'objs':objs})
def about(requests):
    stores_ip(requests)
    return render(requests, 'pages/about.html')
def contact(requests):
    form = forms.ContactForm
    stores_ip(requests)

    if requests.method == 'POST':
        form = forms.ContactForm(requests.POST)
        if form.is_valid():
            form.save()
            sendemail('You have recieved a new contact form', f"Hey, you have recieved a new contact form with a name of {form.cleaned_data['name']} and email {form.cleaned_data['email']}")

            # send an email
    return render(requests, 'pages/contact.html', {'form':form})