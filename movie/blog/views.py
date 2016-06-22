from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from blog.models import Blog
from .forms import BlogForm
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
    data = Blog.objects.all()
    return TemplateResponse(request,'blog/index.html',{"data": data})


def blog(request):
    #we take as request the form containing the blog
    form = BlogForm(request.POST)


    if form.is_valid():
        title = form.cleaned_data['title']
        blog = form.cleaned_data['blog']
        post = Blog.objects.create(title=title, body = blog)

    data = Blog.objects.all()
    return TemplateResponse(request,'blog/index.html',{"data": data})






# Create your views here.
def add_blog(request):
	return render(request,'blog/add_blog.html')

def add(request):
    if 'q' in request.GET:
        message = 'Your blog: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)

def get_blog(request):
    print "we are here"
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print "again"
        # create a form instance and populate it with data from the request:
        form = BlogForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BlogForm()

    return render(request, 'blog/blog.html', {'form': form})

