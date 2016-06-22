from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from video.models import Video

# Create your views here.
def video(request):
    #message = "Hello Meniawy"
    #html = "<html><body><h1> %s.</h1></body></html>" % message
    #return HttpResponse(html)
    data = Video.objects.all()
    return TemplateResponse(request,'video/index.html',{"data": data})


