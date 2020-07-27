from django import forms
from . import models
class Register(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'name':'cName', 'id':'cName','class':'full-width'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password', 'name':'cName', 'id':'cName','class':'full-width'}))
    class Meta():
        model = models.MyUser
        fields = ['email','name']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Name', 'name':'cName', 'id':'cName','class':'full-width'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email', 'name':'cEmail', 'id':'cEmail','class':'full-width'}),
       }
    def saveacc(self, instance):
        userr = models.MyUser(email=instance.cleaned_data.get('email'),name=instance.cleaned_data.get('name'))
        userr.set_password(instance.cleaned_data.get('password'))
        userr.save()

class Login(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'Email', 'name':'cName', 'id':'cName','class':'full-width'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password', 'name':'cName', 'id':'cName','class':'full-width'}))
