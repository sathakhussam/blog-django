from django.urls import path
from . import views
urlpatterns = [
    path('<int:blog_id>/', views.blog_post, name='blogpost'),
    path('update/<int:blog_id>/', views.update_post, name='updatepost'),
    path('delete/<int:blog_id>/', views.delete_post, name='deletepost'),
    path('comments/<int:blog_id>/', views.comments_post, name='commentspost'),
    # this are all for approving
    path('comments/<int:blog_id>/<int:comment_id>/', views.approve_comments, name='approvecomment'),
    path('comments/<int:blog_id>/<int:comment_id>/dis', views.disapprove_comments, name='disapprovecomment'),
    
    path('post/<int:blog_id>/app', views.approve_post, name='approvepost'),
    path('post/<int:blog_id>/dis', views.disapprove_post, name='disapprovepost'),
    # like post 
    path('post/like/<int:blog_id>', views.like_post, name='likepost'),
    path('post/dislike/<int:blog_id>', views.dislike_post, name='dislikepost'),

    path('create/', views.create_post, name='createpost'),
]