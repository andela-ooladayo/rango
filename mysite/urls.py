"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
import settings
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/rango/'

urlpatterns = [
    url(r'^500/$', TemplateView.as_view(template_name="404.html")),
    url(r'^404/$', TemplateView.as_view(template_name="404.html")),
    url(r'^$', 'users.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('users.urls', namespace="users")),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^blog/', include('blog.urls', namespace="blog")),
    url(r'^rango/', include('rango.urls', namespace="rango")),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_DIR}),
]

urlpatterns += staticfiles_urlpatterns()


