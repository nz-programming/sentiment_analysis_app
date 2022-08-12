from django.shortcuts import render
from .models import Main
import json


def gorira(request):
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

    # if request.method == "POST":
    #     if "week_button" in request.POST:
    #         print("week_button")
    #     elif "month_button" in request.POST:
    #         print("month_button")
    #     elif "year_button" in request.POST:
    #         print("year_button")
    
    if request.method == "GET":
        if "week_button" in request.GET:
            print("GET week_button")
        elif "month_button" in request.GET:
            print("GET month_button")
        elif "year_button" in request.GET:
            print("GET year_button")

    return render(request, template_name, context)

