from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(
        r'^$',
        'blog.views.index',
        name = 'index'),
    url(
        r'^post/(?P<pk>[0-9]+)/$', 
        'blog.views.view_post', 
        name='post'),
    url(
        r'^category/(?P<pk>[0-9]+)/$', 
        'blog.views.view_category', 
        name='category'),
    
]