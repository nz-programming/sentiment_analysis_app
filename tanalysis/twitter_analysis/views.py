from django.shortcuts import render
from .models import Main
import json

def index(request):
    template_name = 'twitter_analysis/index.html'
    labels = []
    data = []
    polality_joson = []

    queryset = Main.objects.all()
    for record in queryset:
        #date
        labels.append(record.date)
        #sentiment score
        data.append(record.average_polality)
        #
        polality_joson.append(record.polality_joson)


    var = {
        'labels': labels,
        'data': data,
        # 'polality_json':polality_joson
    }

    context = {'data_json':json.dumps(var, default=str)}

    return render(request, template_name, context)
