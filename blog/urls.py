from django.urls import path
from . import views


urlpatterns = [
    path('postComment', views.postComment, name='postComment'),

    path('', views.blogindex, name='blogindex'),
    path('<str:slug>', views.blogpost, name='blogpost'),
]