from django.shortcuts import render
from django.shortcuts import render_to_response
from app.models import *

# Create your views here.

def blog_list(request):
    blogs = Blog.objects.all()
    return render_to_response("list.html", {"blogs": blogs})