from tkinter import Variable
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Main

import json

# def index(req):
#     # return HttpResponse('Hello World')
#     return render(req, 'twitter_analysis/index.html')

def index(request):
    template_name = 'twitter_analysis/index.html'
    labels = []
    data = []

    context ={}
    queryset = Main.objects.all()

    for main in queryset:
        labels.append(main.date)
        data.append(main.average_polality)

    var = {
        'labels': labels,
        'data': data,
    }
    
    context = {'data_json':json.dumps(var, default=str)}

    return render(request, template_name, context)