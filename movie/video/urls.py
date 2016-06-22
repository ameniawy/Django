from django.conf.urls import url, include
from django.contrib import admin
from video import views


urlpatterns = [
    url(r'^$', views.video, name='video'),

]