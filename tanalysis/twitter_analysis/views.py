from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(req):
    # return HttpResponse('Hello World')
    return render(req, 'twitter_analysis/index.html')
