from django import forms
from . import models
class CommentForm(forms.ModelForm):
    class Meta():
        model = models.Comment
        fields = ['name','email','message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Name',  'id':'cName','class':'full-width'}),
            'email': forms.EmailInput(attrs={'placeholder':'Email',  'id':'cEmail','class':'full-width'}),
            'message': forms.Textarea(attrs={'placeholder':'Your Comment',  'id':'cMessage','class':'full-width'}),
        }
    def savepost(self, request, instance,post):
        post = models.Comment(post=post,name=instance.cleaned_data['name'],email=instance.cleaned_data['email'],message=instance.cleaned_data['message'])
        post.save()
        print('saved')
class PostForm(forms.ModelForm):
    class Meta():
        model = models.BlogPost
        fields = ['title','description','image','quote','quote_writer']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Title', 'id':'cName','class':'full-width'}),
            'image': forms.FileInput(attrs={'accept':'image/*', 'id':'cEmail','class':'full-width'}),
            'description': forms.Textarea(attrs={'placeholder':'Your Content', 'name':'cMessage', 'id':'cMessage','class':'full-width'}),
            'quote': forms.TextInput(attrs={'placeholder':'Quote',  'id':'cName','class':'full-width'}),
            'quote_writer': forms.TextInput(attrs={'placeholder':'Quote Writer', 'id':'cName','class':'full-width'}),
        }
    def savepost(self, request, instance):
        post = models.BlogPost(title=instance.cleaned_data['title'],description=instance.cleaned_data['description'],image=request.FILES['image'])
        post.quote = instance.cleaned_data['quote']
        post.quote_writer = instance.cleaned_data['quote_writer']
        post.author = request.user
        post.save()
        print('saved')