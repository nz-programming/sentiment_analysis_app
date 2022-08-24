from django.shortcuts import render
from ..models import Main
import json

def index(request):
    template_name = 'twitter_analysis/index.html'
    labels = []
    average_polality = []
    polality_joson = []
    retweet_json = []
    keyword_count = []

    queryset = Main.objects.all()
    for record in queryset:
        #date
        labels.append(record.date)
        #sentiment score
        average_polality.append(record.average_polality)
        #JSON for sentiment score ranking
        polality_joson.append(record.polality_joson)
        #JSON for number of retweet ranking
        retweet_json.append(record.retweet_json)
        #JSON for number of keyword ranking
        keyword_count.append(record.keyword_count)
        #
        
    print(f"typeofpolality_joson:{type(record.polality_joson)}")
    print(type(polality_joson))
    print(type(json.dumps(polality_joson, default=str)))
    var = {
        'labels': labels,
        'average_polality': average_polality,
        'polality_json':polality_joson,
        'retweet_json':retweet_json,
        'keyword_count':keyword_count
    }
    
    dataset = {'data_json':json.dumps(var, default=str)}
    print(type(dataset))
    return render(request, template_name, dataset)