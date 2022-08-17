from django.shortcuts import render
from .models import Main
import json

def index(request):
    template_name = 'twitter_analysis/index.html'
    labels = []
    data = []
    context ={}
    # queryset = Main.objects.all()
    # for record in queryset:
    #     df_sentiment_analysis=pd.DataFrame([t['date'] for t in record.date], columns=['date'])
    #     df_sentiment_analysis['average_polality']=[t['average_polality'] for t in record.average_polality]
    # print(df_sentiment_analysis)
    

    if request.method == "GET":
        if "week_button" in request.GET:
            print("GET week button")

        elif "month_button" in request.GET:
            print("GET month_button")

        elif "year_button" in request.GET:
            queryset = Main.objects.all()
            for record in queryset:
                labels.append(record.date)
                data.append(record.average_polality)

            var = {
                'labels': labels,
                'data': data,
            }

            context = {'data_json':json.dumps(var, default=str)}
            print("GET year_button")

        # else:
        #     print("GET year_button")
    # if request.method == "POST":
    #     if "week_button" in request.POST:
    #         print("week_button")
    #     elif "month_button" in request.POST:
    #         print("month_button")
    #     elif "year_button" in request.POST:
    #         print("year_button")
    
    # if request.method == "GET":
    #     if "week_button" in request.GET:
    #         print("GET week_button")
    #     elif "month_button" in request.GET:
    #         print("GET month_button")
    #     elif "year_button" in request.GET:
    #         print("GET year_button")

    return render(request, template_name, context)
