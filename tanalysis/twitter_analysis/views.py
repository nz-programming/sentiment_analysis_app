from django.shortcuts import render
from .models import Main
import json

def index(request):
    template_name = 'twitter_analysis/index.html'
    labels = []
    average_polality = []
    polality_joson = []
    keyword_count = []
    id = []

    queryset = Main.objects.all()
    for record in queryset:
        #date
        labels.append(record.date)
        #sentiment score
        average_polality.append(record.average_polality)
        #
        polality_joson.append(record.polality_joson)
        #
        keyword_count.append(record.keyword_count)
        #
        id.append(record.id)
    print(f"typeofpolality_joson:{type(record.polality_joson)}")
    # print(f"labels:{labels}")
    # print(f"average_polality:{average_polality}")
    # print(f"polality_joson:{polality_joson}")
    print(type(polality_joson))
    print(type(json.dumps(polality_joson, default=str)))
    var = {
        'labels': labels,
        'average_polality': average_polality,
        'polality_json':polality_joson,
        'keyword_count':keyword_count
        # 'id': id
    }
    
    dataset = {'data_json':json.dumps(var, default=str)}
    print(type(dataset))
    return render(request, template_name, dataset)
