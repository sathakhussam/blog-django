from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required   
from . import forms
from blog import models
from pages.models import ContactForm
from blessedbb.own import stores_ip
# Create your views here.
@login_required
def register(request):
    stores_ip(request)
    if request.user.is_admin:
        form = forms.Register
        if request.method == 'POST':
            form = forms.Register(request.POST)
            if form.is_valid():
                form.save(commit=False)
                if form.cleaned_data['password'] == form.cleaned_data['password_confirm']:
                    # form.save()
                    print(form.saveacc(form))
                else:
                    return render(request, 'accounts/register.html', {'form':form, 'error':"The passwords didn't matched"})
        return render(request, 'accounts/register.html', {'form':form})
    return Http404()

def Mylogin(request):
    stores_ip(request)
    form = forms.Login
    if request.method == 'POST':
        form = forms.Login(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            userr = authenticate(email=email, password=password)
            login(request, userr)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'form':form, 'error':"Sorry Credentials Didn't matched"})

    return render(request, 'accounts/login.html', {'form':form})
@login_required
def Customadmin(request):
    context = {}
    if request.user.is_admin:
        context['admin'] = True
        context['objs'] = models.BlogPost.objects.all
        context['forms'] = ContactForm.objects.all
    else:
        context['author'] = True
        context['objs'] = models.BlogPost.objects.filter(author=request.user)
    return render(request, 'accounts/admin.html',context)

@login_required
def eachform(request, form_id):
    context = {}
    if request.user.is_admin:
        form = get_object_or_404(ContactForm, id=form_id)
        context['eachform'] = form
    return render(request, 'accounts/eachform.html',context)