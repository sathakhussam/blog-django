from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from . import forms ,models
from blessedbb.own import stores_ip
from blog.function import sendemail


# Create your views here.
def blog_post(request,blog_id):
    stores_ip(request)
    context = {}
    obj = get_object_or_404(models.BlogPost,id=blog_id) 
    comments = models.Comment.objects.filter(post=obj ,is_published=False)
    print(comments)
    context['obj'] = obj
    context['comments'] = comments
    obj_prev = models.BlogPost.objects.filter(id__lt=blog_id)[0:1]
    obj_next = models.BlogPost.objects.filter(id__gt=blog_id)[0:1]
    if obj_prev:
        context['obj_prev']=obj_prev
    if obj_next:
        context['obj_next']=obj_next
    form = forms.CommentForm
    context['form'] = form
    if 'liked'in  request.session:
        if blog_id in request.session['liked']:
            context['liked'] = True
    elif 'disliked' in request.session:
        if blog_id in request.session['liked']:
            context['disliked'] = True
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            form.savepost(request,form,obj)
            sendemail('You have recieved a new comment', f"Hello there, you have recieved new comment from {form.cleaned_data['name']} and for the post {obj.title}")
    return render(request, 'blog/post.html', context)

@login_required
def create_post(request):
    stores_ip(request)
    form = forms.PostForm
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            print('from valid')
            form.savepost(request , form) 
            return sendemail("There's a new post in your website ", f"Hello There, you have a new post in the website with the title {form.cleaned_data['title']} and by {request.user.name} and it havent published yet.")
            return redirect('admin')
            # send an email
    return render(request, 'blog/create_post.html', {'form': form})
@login_required
def update_post(request,blog_id):
    stores_ip(request)
    # if reque
    obj = get_object_or_404(models.BlogPost,id=blog_id) 
    if request.user == obj.author or request.user.is_admin:
        form = forms.PostForm(request.POST or None, instance = obj)
        if form.is_valid(): 
            form.savepost(request,form) 
            return redirect('admin')
    return render(request, "blog/update_post.html", {'form': form, 'obj':obj}) 

@login_required
def delete_post(request,blog_id):
    obj = get_object_or_404(models.BlogPost,id=blog_id) 
    if request.user == obj.author or request.user.is_admin:
        obj.delete()

@login_required
def comments_post(request,blog_id):
    obj = get_object_or_404(models.BlogPost, id=blog_id) 

    if request.user == obj.author or request.user.is_admin:
        comments = models.Comment.objects.filter(post=obj)
        return render(request, 'blog/comments.html',{'obj':obj,'comments':comments})

@login_required
def approve_comments(request,blog_id,comment_id):
    obj = get_object_or_404(models.Comment, id=comment_id)
    if request.user == obj.post.author or request.user.is_admin:
        obj.is_published = True
        obj.save()
        return redirect('commentspost', blog_id)

@login_required
def disapprove_comments(request,blog_id,comment_id):
    obj = get_object_or_404(models.Comment, id=comment_id)
    if request.user == obj.post.author or request.user.is_admin:
        obj.is_published = False
        obj.save()
        return redirect('commentspost', blog_id)


@login_required
def approve_post(request,blog_id):
    obj = get_object_or_404(models.BlogPost, id=blog_id)
    if request.user == obj.author or request.user.is_admin:
        obj.is_published = True
        obj.save()
        return redirect('admin')
@login_required
def disapprove_post(request,blog_id):
    obj = get_object_or_404(models.BlogPost, id=blog_id)
    if request.user == obj.author or request.user.is_admin:
        obj.is_published = False
        obj.save()
        return redirect('admin')


# likes post 
@login_required
def like_post(request,blog_id):
    obj = get_object_or_404(models.BlogPost, id=blog_id)
    sendemail('Hey you have a new like',f'Hello, you have recieved a like in the post {obj.title}')
    if 'liked' in request.session:
        liked_posts = request.session['liked']
        liked_posts.append(blog_id)
        request.session['liked'] = liked_posts
        obj.likes += 1
        obj.save()
        return redirect('blogpost', blog_id)
    else: 
        liked_posts = []
        liked_posts.append(blog_id)
        request.session['liked'] = liked_posts
        obj.likes += 1
        obj.save()
        return redirect('blogpost', blog_id)
@login_required
def dislike_post(request,blog_id):
    sendemail('Hey you have a new dislike',f'Hello, you have recieved a dislike in the post {obj.title}')
    obj = get_object_or_404(models.BlogPost, id=blog_id)
    if 'disliked' in request.session:
        disliked_posts = request.session['disliked']
        disliked_posts.append(blog_id)
        request.session['disliked'] = disliked_posts
        obj.dislikes += 1
        obj.save()
        return redirect('blogpost', blog_id)
    else: 
        disliked_posts = []
        disliked_posts.append(blog_id)
        request.session['disliked'] = disliked_posts
        obj.dislikes += 1
        obj.save()
        return redirect('blogpost', blog_id)
