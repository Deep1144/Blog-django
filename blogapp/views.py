from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import blog
from django.contrib import messages
# Create your views here.
def index(request):

    blogs  = blog.objects.all()
    return render(request,'index.html' , {'blogs' : blogs})

def read(request,blogid):
    blogs  = blog.objects.get(id=blogid)
    return render(request,'read.html' , {'blog':blogs})

def upload(request):
    if request.method == 'POST':
        img = request.FILES['img']
        img2 = request.FILES['img2']
        title = request.POST.get('title')
        subtitle = request.POST.get('subtitle')
        sub2title = request.POST.get('sub2title')
        content_at = request.POST.get('content_at')
        content_as = request.POST.get('content_as')
        content_as2 = request.POST.get('content_as2')
        
        Blog = blog(img=img, img2=img2 , title=title ,subtitle=subtitle ,sub2title=sub2title,content_as=content_as,content_as2=content_as2,content_at=content_at)
        Blog.save()
        messages.info(request,'Blog posted')
        return redirect('/')
      
    return render(request,'upload.html')

