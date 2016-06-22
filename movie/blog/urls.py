from django.conf.urls import url, include
from django.contrib import admin
from blog import views


urlpatterns = [
    url(r'^$', views.blog, name='blog'),
    url(r'^add/$',views.add_blog, name='addblog')

]