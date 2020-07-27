from django.db import models
from django.utils import timezone
from accounts.models import MyUser
from blog.function import sendemail
# Create your models here.


class BlogPost(models.Model):
    author = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(max_length=1000)
    description = models.TextField()
    image = models.ImageField(upload_to='%Y/%m/%d/')
    quote = models.CharField(max_length=1000, blank=True, null=True)
    quote_writer = models.CharField(max_length=1000, blank=True, null=True)
    is_published = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=256)
    email = models.EmailField()
    message = models.TextField()
    is_published = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.name} ({self.email})'
class like(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.DO_NOTHING, null=True)
    
class dislike(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.DO_NOTHING, null=True)










    
