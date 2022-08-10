from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Main

# def index(req):
#     # return HttpResponse('Hello World')
#     return render(req, 'twitter_analysis/index.html')

def index(req):
    template_name = 'twitter_analysis/index.html'
    ctx ={}
    qs = Main.objects.all()
    ctx["object_list"] =qs
    return render(req, template_name, ctx)