from django.shortcuts import render
from django.shortcuts import render_to_response
from app.models import *
from django.http import Http404
# Create your views here.

def list(request):
    blogs = Blog.objects.all()
    return render_to_response("list.html", {"blogs": blogs})

def  index(request):
	return render_to_response('index.html')

def blogarticle(request,id=''):
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response("blogarticle.html", {"blog":blog})