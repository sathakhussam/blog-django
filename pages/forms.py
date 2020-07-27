from django import forms
from . import models
class ContactForm(forms.ModelForm):
    class Meta():
        model = models.ContactForm
        fields = ['name','email','message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Name', 'name':'cName', 'id':'cName','class':'full-width'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email', 'name':'cEmail', 'id':'cEmail','class':'full-width'}),
            'message': forms.Textarea(attrs={'placeholder':'Your Message', 'name':'cMessage', 'id':'cMessage','class':'full-width'}),
        }